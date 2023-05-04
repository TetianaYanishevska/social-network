from flask_restful import Resource
from flask import jsonify, request

from app import db
from app.models import Post, Like
from app.schemas import PostSchema, LikeSchema
from flask_login import current_user
from flask_jwt_extended import jwt_required


class PostsResource(Resource):
    def get(self):
        author_id = request.args.get('author_id', type=int)
        query = db.session.query(Post)
        if author_id:
            query = query.filter(Post.author_id == author_id)
        posts = query.all()
        return jsonify(PostSchema().dump(posts, many=True))

    def post(self):
        json_data = request.get_json()
        if json_data['author_id'] != current_user.id:
            response = jsonify(error="Post author not match")
            response.status_code = 400
            return response

        new_post = PostSchema.load(json_data)
        return jsonify(PostSchema().dump(new_post, many=False))


class PostResource(Resource):
    method_decorators = [jwt_required()]

    def get(self, post_id):
        post = db.session.query(Post).filter(Post.id == post_id).first_or_404()
        return jsonify(PostSchema().dump(post, many=False))

    def put(self, post_id):
        json_data = request.get_json()
        json_data['id'] = post_id
        updated_post = PostSchema().load(json_data)
        db.session.add(updated_post)
        db.session.commit()
        return jsonify(PostSchema().dump(updated_post, many=False))

    def delete(self, post_id):
        post = db.session.query(Post).filter(Post.id == post_id).first_or_404()
        db.session.delete(post)
        db.session.commit()
        return jsonify(success=True)


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

        new_like = jsonify(LikeSchema().load(json_data))
        return jsonify(LikeSchema().dump(new_like, many=False))
