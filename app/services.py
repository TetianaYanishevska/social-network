from app import db
from app.models import User, Profile, Post, Like, Dislike
from app.schemas import UserSchema, PostSchema, ProfileSchema
from flask_login import current_user
from flask import jsonify


class UserService:
    def get_by_id(self, user_id):
        user = db.session.query(User).filter(User.id == user_id).first_or_404()
        return user

    def get_by_username(self, username):
        user = db.session.query(User).filter(User.username == username).first_or_404()
        return user

    def create(self, **kwargs):
        user = User(username=kwargs.get('username'), email=kwargs.get('email'))
        user.set_password(kwargs.get('password'))
        db.session.add(user)
        db.session.commit()
        profile = Profile(user_id=user.id)
        db.session.add(profile)
        db.session.commit()
        return user

    def update(self, data):
        user = self.get_by_id(data['id'])
        data['profile']['id'] = user.profile.id
        data['profile']['user_id'] = user.id
        user = UserSchema(exclude=('password',)).load(data)
        db.session.add(user)
        db.session.commit()
        return user

    def delete(self, user_id):
        user = self.get_by_id(user_id)
        profile = user.profile
        db.session.delete(profile)
        db.session.commit()
        db.session.delete(user)
        db.session.commit()
        return True


class PostService:
    def get_by_author(self, author_id):
        query = db.session.query(Post)
        if author_id:
            query = query.filter(Post.author_id == author_id)
        posts = query.all()
        return posts

    def get_by_id(self, post_id):
        post = db.session.query(Post).filter(Post.id == post_id).first_or_404()
        return post

    def create(self, **kwargs):
        if kwargs.get('author_id') != current_user.id:
            response = jsonify(error="Post author not match")
            response.status_code = 400
            return response
        new_post = Post(author_id=kwargs.get('author_id'), title=kwargs.get('title'), content=kwargs.get('content'))
        db.session.add(new_post)
        db.session.commit()
        return new_post

    def update(self, data):
        updated_post = PostSchema().load(data)
        db.session.add(updated_post)
        db.session.commit()
        return updated_post

    def delete(self, post_id):
        post = self.get_by_id(post_id)
        db.session.delete(post)
        db.session.commit()
        return True


class ProfileService(UserService):
    def get(self, user_id):
        user = super().get_by_id(user_id)
        profile = user.profile
        return profile

    def update(self, data):
        user = super().get_by_id(data['user_id'])
        data['id'] = user.profile.id
        data['user_id'] = user.id
        profile = ProfileSchema().load(data)
        db.session.add(profile)
        db.session.commit()
        return profile


class LikeService:
    def create(self, **kwargs):
        post_id = kwargs.get('post_id')
        user_id = kwargs.get('user_id')
        like = (db.session.query(Like)
                .filter(Like.post_id == post_id,
                        Like.user_id == user_id)
                ).first()
        if like:
            return False
        new_like = Like(user_id=user_id, post_id=post_id)
        db.session.add(new_like)
        db.session.commit()
        return new_like


class DislikeService:
    def create(self, **kwargs):
        post_id = kwargs.get('post_id')
        user_id = kwargs.get('user_id')
        dislike = (db.session.query(Dislike)
                   .filter(Dislike.post_id == post_id,
                           Dislike.user_id == user_id)
                   ).first()
        if dislike:
            return False
        new_dislike = Dislike(user_id=user_id, post_id=post_id)
        db.session.add(new_dislike)
        db.session.commit()
        return new_dislike
