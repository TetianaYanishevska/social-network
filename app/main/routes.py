from app.main import bp
from flask import render_template


@bp.route("/")
@bp.route("/index")
def index():
    context = {
        "user": {"username": "Tetiana"},
        "title": "Hillel"
    }
    return render_template("index.html", **context)


@bp.route("/about")
def about():
    context = {
        "page": "About",
        "title": "Hillel"
    }
    return render_template("about.html", **context)
    

