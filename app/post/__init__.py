import click as click
from flask import Blueprint

from .. import db
from ..models import User
import os
import csv

bp = Blueprint('post', __name__, url_prefix='/post')

from . import routes # noqa


@bp.cli.command('extract_posts')
@click.argument('user_id', type=int)
def extract_posts(user_id):

    user = db.session.query(User).filter(User.id == user_id).first()
    if not user:
        print("There is no user with that id in the database")
    else:
        user_posts_data = []
        for post in user.posts:
            post_data = {
                        'Title': post.title,
                        'Created_at': post.created_at.strftime('%d.%m.%Y %H:%M'),
                        'Number_of_likes': len(post.likes),
                        'Number_of_dislikes': len(post.dislikes)
                        }
            user_posts_data.append(post_data)

        current_directory = os.getcwd()
        file_name = f"{user.username}_posts.csv"
        file_path = os.path.join(current_directory, file_name)

        with open(file_path, mode='w', newline='') as file:
            fieldnames = ['Title', 'Created_at', 'Number_of_likes', 'Number_of_dislikes']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(user_posts_data)
