import click
from flask import Blueprint
from faker import Faker

from app import db
from app.models import User, Profile

bp = Blueprint('fake', __name__)
faker = Faker()


@bp.cli.command("users")
@click.argument('num', type=int)
def users(num):
    for i in range(num):
        username = faker.user_name()
        email = faker.email()
        password = faker.password()
        created_at = faker.date_time_this_year()
        first_name = faker.first_name()
        last_name = faker.last_name()
        about_me = faker.paragraph()
        linkedin = f'https://facebook.com/{username}'
        facebook = f'https://linkedin.com/{username}'
        user = (
            db.session.query(User)
            .filter(
                User.username == username,
                User.email == email
            )
        ).first()
        if not user:
            user = User(
                username=username,
                email=email,
                password=password,
                created_at=created_at
            )
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            profile = Profile(user_id=user.id,
                              first_name=first_name,
                              last_name=last_name,
                              about_me=about_me,
                              linkedin=linkedin,
                              facebook=facebook
                              )
            db.session.add(profile)
            db.session.commit()
    print(num, 'users added.')
