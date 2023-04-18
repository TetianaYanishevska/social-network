from app import db
from app.main import bp
from flask import render_template
from app.models import User


@bp.route("/")
@bp.route("/index")
def index():
    users_query = db.session.query(User)
    users = users_query.all()
    return render_template("index.html", users=users)


@bp.route("/about")
def about():
    context = {
        "page": "About",
        "title": "Hillel"
    }
    return render_template("about.html", **context)
