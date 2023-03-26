from app import app
from flask import render_template


@app.route("/")
@app.route("/index")
def index():
    context = {
        "user": {"username": "Tetiana"},
        "title": "Hillel"
    }
    return render_template("index.html", **context)


@app.route("/about")
def about():
    context = {
        "page": "About",
        "title": "Hillel"
    }
    return render_template("about.html", **context)
    

