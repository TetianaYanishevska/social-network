from flask_restful import Resource
from flask import jsonify, request

from app import db
from app.models import Like, Dislike
from app.schemas import LikeSchema, DislikeSchema
from app.services import LikeService, DislikeService

like_service = LikeService()
dislike_service = DislikeService()


class LikesResource(Resource):
    def get(self):
        likes = db.session.query(Like).all()
        return jsonify(LikeSchema().dump(likes, many=True))


class LikeResource(Resource):
    def get(self, like_id):
        like = db.session.query(Like).filter(Like.id == like_id).first_or_404()
        return jsonify(LikeSchema().dump(like, many=False))

    def post(self):
        json_data = request.get_json()
        new_like = like_service.create(**json_data)
        if not new_like:
            response = jsonify(error="Like has already been set")
            response.status_code = 400
            return response
        else:
            response = jsonify(LikeSchema().dump(new_like, many=False))
            response.status_code = 201
            return response


class DislikesResource(Resource):
    def get(self):
        dislikes = db.session.query(Dislike).all()
        return jsonify(DislikeSchema().dump(dislikes, many=True))


class DislikeResource(Resource):
    def get(self, dislike_id):
        dislike = db.session.query(Dislike).filter(Dislike.id == dislike_id).first_or_404()
        return jsonify(DislikeSchema().dump(dislike, many=False))

    def post(self):
        json_data = request.get_json()
        new_dislike = dislike_service.create(**json_data)
        if not new_dislike:
            response = jsonify(error="Dislike has already been set")
            response.status_code = 400
            return response
        else:
            response = jsonify(DislikeSchema().dump(new_dislike, many=False))
            response.status_code = 201
            return response
