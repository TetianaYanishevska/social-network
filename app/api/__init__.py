from flask import Blueprint
from flask_restful import Api

from app.api.auth import GenerateTokenResource
from app.api.post import PostsResource, PostResource, LikeResource, DislikeResource
from app.api.user import UsersResource, UserResource


bp = Blueprint('api', __name__, url_prefix="/api")
api = Api(bp)
api.add_resource(UsersResource, '/users', endpoint="users_list")
api.add_resource(UserResource, '/users/<int:user_id>', endpoint="users_details")

api.add_resource(PostsResource, '/posts', endpoint="posts_list")
api.add_resource(PostResource, '/posts/<int:post_id>', endpoint="posts_details")

api.add_resource(GenerateTokenResource, '/generate-token', endpoint="generate_token")

api.add_resource(LikeResource, '/posts/like', endpoint="post_likes")

api.add_resource(DislikeResource, '/posts/dislike', endpoint="post_dislikes")
