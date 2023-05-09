from flask import Blueprint
from flask_restful import Api

from app.api.auth import GenerateTokenResource
from app.api.post import PostsResource, PostResource
from app.api.like_dislike import LikesResource, LikeResource, DislikesResource, DislikeResource
from app.api.user import UsersResource, UserResource, ProfileResource

bp = Blueprint('api', __name__, url_prefix="/api")
api = Api(bp)
api.add_resource(UsersResource, '/users', endpoint="users_list")
api.add_resource(UserResource, '/users/<int:user_id>', endpoint="users_details")

api.add_resource(ProfileResource, '/users/<int:user_id>/profile', endpoint="profiles_details")

api.add_resource(PostsResource, '/posts', endpoint="posts_list")
api.add_resource(PostResource, '/posts/<int:post_id>', endpoint="posts_details")

api.add_resource(GenerateTokenResource, '/generate-token', endpoint="generate_token")

api.add_resource(LikesResource, '/posts/likes', endpoint="post_likes")
api.add_resource(LikeResource, '/posts/like', '/posts/likes/<int:like_id>', endpoint="post_like")

api.add_resource(DislikesResource, '/posts/dislikes', endpoint="post_dislikes")
api.add_resource(DislikeResource, '/posts/dislike', '/posts/dislikes/<int:dislike_id>', endpoint="post_dislike")
