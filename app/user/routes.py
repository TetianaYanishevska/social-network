from app.user import bp
from .forms import ProfileForm
from .. import db
from ..models import User
from flask_login import login_required
from flask import render_template, flash, redirect, url_for, request


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
