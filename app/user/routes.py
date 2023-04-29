from app.user import bp
from .forms import ProfileForm
from .. import db
from ..models import User, Post, Follow
from flask_login import login_required, current_user
from flask import render_template, flash, redirect, url_for, request

from ..post.forms import PostForm


@bp.route("/blog")
@login_required
def blog():
    form = PostForm()
    posts = (
        db.session.query(Post)
        .filter(
            Post.author_id == current_user.id
        )
        .order_by(Post.created_at.desc())
        .all()
    )
    return render_template("user/blog.html", posts=posts, form=form)


@bp.route("/profile/<string:username>", methods=['GET', 'POST'])
@login_required
def profile(username):
    user = db.session.query(User).filter(User.username == username).first_or_404()
    form = ProfileForm()
    if form.validate_on_submit():
        user.profile.first_name = form.first_name.data
        user.profile.last_name = form.last_name.data
        user.profile.about_me = form.about_me.data
        user.profile.linkedin = form.linkedin.data
        user.profile.facebook = form.facebook.data
        db.session.commit()
        flash('Your changes have been saved', category="success")
        return redirect(url_for('user.profile', username=user.username))
    elif request.method == 'GET':
        form.first_name.data = user.profile.first_name
        form.last_name.data = user.profile.last_name
        form.about_me.data = user.profile.about_me
        form.linkedin.data = user.profile.linkedin
        form.facebook.data = user.profile.facebook
    return render_template('user/profile.html', user=user, form=form)


@bp.route('/<int:user_id>/follow', methods=['POST'])
@login_required
def follow(user_id):
    to_follow = Follow(follower_id=current_user.id, followee_id=user_id)
    db.session.add(to_follow)
    db.session.commit()
    flash('You are now following this user!', 'success')
    return redirect(request.referrer)


@bp.route('/<int:user_id>/unfollow', methods=['GET', 'POST'])
@login_required
def unfollow(user_id):
    to_unfollow = db.session.query(Follow).filter(db.and_(
        Follow.follower_id == current_user.id,
        Follow.followee_id == user_id)
    ).first()
    if to_unfollow:
        db.session.delete(to_unfollow)
        db.session.commit()
        flash('You are no longer following this user!', 'success')
    return redirect(request.referrer)
