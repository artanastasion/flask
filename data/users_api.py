import flask
from flask import jsonify

from . import db_session
from .users import User

blueprint = flask.Blueprint(
    'users_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/users')
def get_users():
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    users_list = [
        {
            "id": user.id,
            "surname": user.surname,
            "name": user.name,
            "age": user.age,
            "position": user.position,
            "speciality": user.speciality,
            "address": user.address,
            "email": user.email,
            "hashed_password": user.hashed_password,
            "modified_date": user.modified_date
        }
        for user in users
    ]
    return jsonify(users_list)
