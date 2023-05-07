from flask_restful import Resource
from flask import jsonify, request

from app import db
from app.models import Like, Dislike
from app.schemas import PostSchema, LikeSchema, DislikeSchema
from flask_login import current_user # noqa
from flask_jwt_extended import jwt_required

from app.services import PostService


post_service = PostService()


class PostsResource(Resource):

    def get(self):
        author_id = request.args.get('author_id', type=int)
        posts = post_service.get_by_author(author_id)
        return jsonify(PostSchema().dump(posts, many=True))

    def post(self):
        json_data = request.get_json()
        new_post = post_service.create(**json_data)
        response = jsonify(PostSchema().dump(new_post, many=False))
        response.status_code = 201
        # if json_data['author_id'] != current_user.id:
        #     response = jsonify(error="Post author not match")
        #     response.status_code = 400
        #     return response

        # new_post = PostSchema().load(json_data)
        # db.session.add(new_post)
        # db.session.commit()
        # return jsonify(PostSchema().dump(new_post, many=False))
        return response


class PostResource(Resource):
    method_decorators = [jwt_required()]

    def get(self, post_id):
        post = post_service.get_by_id(post_id)
        return jsonify(PostSchema().dump(post, many=False))

    def put(self, post_id):
        json_data = request.get_json()
        json_data['id'] = post_id
        updated_post = post_service.update(json_data)
        return jsonify(PostSchema().dump(updated_post, many=False))

    def delete(self, post_id):
        status = post_service.delete(post_id)
        return jsonify(status=status)


class LikeResource(Resource):
    def post(self):
        json_data = request.get_json()
        post_id = json_data['post_id']
        user_id = json_data['user_id']
        like = (db.session.query(Like)
                .filter(Like.post_id == post_id,
                        Like.user_id == user_id)
                ).first()
        if like:
            response = jsonify(error="Like has already been set")
            response.status_code = 400
            return response
        new_like = LikeSchema().load(json_data)
        db.session.add(new_like)
        db.session.commit()
        return jsonify(LikeSchema().dump(new_like, many=False))


class DislikeResource(Resource):
    def post(self):
        json_data = request.get_json()
        post_id = json_data['post_id']
        user_id = json_data['user_id']
        dislike = (db.session.query(Dislike)
                   .filter(Dislike.post_id == post_id,
                           Dislike.user_id == user_id)
                   ).first()
        if dislike:
            response = jsonify(error="Dislike has already been set")
            response.status_code = 400
            return response

        new_dislike = DislikeSchema().load(json_data)
        db.session.add(new_dislike)
        db.session.commit()
        return jsonify(DislikeSchema().dump(new_dislike, many=False))
