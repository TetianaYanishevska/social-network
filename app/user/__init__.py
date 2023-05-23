from flask import Blueprint

from .. import db
from ..models import User
import os
import csv

bp = Blueprint('user', __name__, url_prefix='/user')

from . import routes # noqa


@bp.cli.command('extract_users')
def extract_users():

    users = db.session.query(User).all()
    if not users:
        print("There is no user in the database")
    else:
        data = []
        for user in users:
            user_data = {'Username': user.username,
                         'Email': user.email,
                         'Full_name': user.profile.full_name,
                         'Number_of_posts': len(user.posts)
                         }
            data.append(user_data)

        current_directory = os.getcwd()
        file_name = "users.csv"
        file_path = os.path.join(current_directory, file_name)

        with open(file_path, mode='w', newline='') as file:
            fieldnames = ['Username', 'Email', 'Full_name', 'Number_of_posts']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
