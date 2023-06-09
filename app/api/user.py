from flask_restful import Resource
from app import db
from app.models import User
from flask import jsonify, request

from app.schemas import UserSchema, ProfileSchema
from app.services import UserService, ProfileService
from flask_jwt_extended import jwt_required

user_service = UserService()
profile_service = ProfileService()


class UsersResource(Resource):
    def get(self):
        users = db.session.query(User).all()
        return jsonify(UserSchema(exclude=("password",)).dump(users, many=True))

    def post(self):
        json_data = request.get_json()
        user = user_service.create(**json_data)
        response = jsonify(UserSchema().dump(user, many=False))
        response.status_code = 201
        return response


class UserResource(Resource):
    def get(self, user_id):
        user = user_service.get_by_id(user_id)
        return jsonify(UserSchema(exclude=("password",)).dump(user, many=False))

    @jwt_required()
    def put(self, user_id):
        json_data = request.get_json()
        json_data['id'] = user_id
        user = user_service.update(json_data)
        return jsonify(UserSchema(exclude=("password",)).dump(user, many=False))

    @jwt_required()
    def delete(self, user_id):
        status = user_service.delete(user_id)
        return jsonify(status=status)


class ProfileResource(Resource):
    def get(self, user_id):
        profile = profile_service.get(user_id)
        return jsonify(ProfileSchema().dump(profile, many=False))

    @jwt_required()
    def put(self, user_id):
        json_data = request.get_json()
        json_data['user_id'] = user_id
        profile = profile_service.update(json_data)
        return jsonify(ProfileSchema().dump(profile, many=False))
