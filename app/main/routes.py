from app import db
from app.main import bp
from flask import render_template
from app.models import User


@bp.route("/")
@bp.route("/index")
def index():

    users_data = [
        {
            "username": "akushyn",
            "email": "akushyn@gmail.com",
            "password": "123456"
        },
        {
            "username": "anton",
            "email": "anton@gmail.com",
            "password": "234567"
        },
        {
            "username": "denys",
            "email": "denys@gmail.com",
            "password": "345678"
        },
        {
            "username": "tanya",
            "email": "tanya@gmail.com",
            "password": "456789"
        },
        {
            "username": "igor",
            "email": "igor@gmail.com",
            "password": "567890"
        }
    ]
    for u in users_data:
        user = (
            db.session.query(User).filter(
                User.username == u.get('username'),
                User.email == u.get('email'),
                User.password == u.get('password')
                ).first()
        )
        if user:
            continue
        user = User(
            username=u.get('username'),
            email=u.get('email'),
            password=u.get('password')
        )
        db.session.add(user)
    db.session.commit()

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
