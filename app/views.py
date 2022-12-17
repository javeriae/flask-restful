"""
Application Views.
"""
from datetime import datetime

from flask import request
from flask_restful import Resource
from werkzeug.security import generate_password_hash

from app.app import basic_auth, db
from app.constants import INVALID_DATA, RESOURCE_NOT_FOUND
from app.helpers import decrypt, encrypt
from app.models import Book, User
from app.schemas import BookSchema, UserSchema
from app.serializers import book_serializer, user_serializer


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

        Returns: string
        """
        users = User.query.all()
        results = [user_serializer(user) for user in users]
        return encrypt({
            'count': len(results),
            'objects': results,
        }), 200

    @basic_auth.login_required
    def post(self):
        """
        Method to create a new user.

        Returns: string
        """
        user_schema = UserSchema()
        errors = user_schema.validate(request.json)

        if errors:
            return INVALID_DATA

        user = User(
            username=request.json.get('username'),
            password=generate_password_hash(request.json.get('password'))
        )
        db.session.add(user)
        db.session.commit()

        return encrypt({
            'message': 'Record added successfully.',
            'resource_id': user.username,
            'status_code': 201
        }), 201


class BookItems(Resource):
    """
    Views to retrieve book objects or add new object.
    """
    @basic_auth.login_required
    def get(self):
        """
        Method to retrieve the list of all books.

        Returns: string
        """
        books = Book.query.all()
        results = [book_serializer(book) for book in books]

        return encrypt({
            'count': len(results),
            'objects': results,
        }), 200

    @basic_auth.login_required
    def post(self):
        """
        Method to create a new book.

        Returns: string
        """
        book_schema = BookSchema()
        errors = book_schema.validate(request.json)

        if errors:
            return INVALID_DATA

        book = Book(
            title=request.json.get('title'),
            description=request.json.get('description'),
            pages=request.json.get('pages'),
            published_on=datetime.strptime(request.json.get('published_on'), '%Y-%m-%d').date()
        )
        db.session.add(book)
        db.session.commit()

        return encrypt({
            'message': 'Record added successfully.',
            'resource_id': book.id,
            'status_code': 201
        }), 201


class BookItem(Resource):
    """
    Views to retrieve a single book object or edit a object.
    """
    @basic_auth.login_required
    def get(self, book_id):
        """
        Method to retrieve data for a single book object.

        Args:
        book_id(int): Book id value provided by user

        Returns: string
        """
        book = Book.query.get(book_id)

        if not book:
            return RESOURCE_NOT_FOUND

        return encrypt(book_serializer(book)), 200

    @basic_auth.login_required
    def put(self, book_id):
        """
        Method to update data for a book object.

        Args:
        book_id(int): Book id value provided by user

        Returns: string
        """
        book = Book.query.get(book_id)

        if not book:
            return RESOURCE_NOT_FOUND

        book_schema = BookSchema()
        errors = book_schema.validate(request.json)

        if errors:
            return INVALID_DATA

        book.title = request.json.get('title')
        book.description = request.json.get('description')
        book.pages = request.json.get('pages')
        book.published_on = datetime.strptime(request.json.get('published_on'), '%Y-%m-%d').date()

        db.session.add(book)
        db.session.commit()

        return encrypt({
            'message': 'Record updated successfully.',
            'resource_id': book.id,
            'status_code': 204
        }), 204

    @basic_auth.login_required
    def delete(self, book_id):
        """
        Method to delete a single book object.

        Args:
        book_id(int): Book id value provided by user

        Returns: string
        """
        book = Book.query.get(book_id)

        if not book:
            return RESOURCE_NOT_FOUND

        db.session.delete(book)
        db.session.commit()

        return encrypt({
            'message': 'Record deleted successfully.',
            'resource_id': book.id,
            'status_code': 204
        }), 204


class DecryptText(Resource):
    """
    Example view to decrypt the text from other endpoints.
    """

    @basic_auth.login_required
    def get(self):
        """
        Method to decrypt the text.

        Args: None

        Returns: dict
        """
        encrypted_text = request.json.get('text')
        return decrypt(encrypted_text), 200
