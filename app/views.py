"""
Application Views.
"""
from flask import request
from flask_restful import Resource
from werkzeug.security import generate_password_hash

from app.app import basic_auth, db
from app.models import User
from app.schemas import UserSchema
from app.serializers import user_serializer


class Index(Resource):
    """
    Example view to test server.
    """
    def get(self):
        """
        Example view to verify that server has started.

        Returns: string
        """
        return 'Server is up & running'


class UserItems(Resource):
    """
    Views for the User Model.
    """
    @basic_auth.login_required
    def get(self):
        """
        Method to retrieve the list of all users.

        Returns: dict
        """
        users = User.query.all()
        results = [user_serializer(user) for user in users]
        return {
            'count': len(results),
            'objects': results,
        }

    @basic_auth.login_required
    def post(self):
        """
        Method to create a new user.\

        Returns: dict
        """
        user_schema = UserSchema()
        errors = user_schema.validate(request.json)

        if errors:
            return {
                       'error_msg': 'Invalid data.',
                       'error_code': 'BAD_REQUEST',
                       'status_code': 400
                   }, 400

        user = User(
            username=request.json.get('username'),
            password=generate_password_hash(request.json.get('password'))
        )
        db.session.add(user)
        db.session.commit()

        return {
            'message': 'Record added successfully.',
            'resource_id': user.username,
            'status_code': 201
        }
