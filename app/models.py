"""
Application Models.
"""
from .app import db


class User(db.Model):  # pylint: disable=too-few-public-methods
    """
    User model for authentication.
    """
    username = db.Column(db.String(128), primary_key=True)
    password = db.Column(db.String(128), nullable=False)

    def __str__(self):
        return self.username


class Book(db.Model):  # pylint: disable=too-few-public-methods
    """
    Model to store the book data
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, default=True, nullable=False)
    pages = db.Column(db.Integer, nullable=False)
    published_on = db.Column(db.Date, nullable=False)

    def __str__(self):
        return self.title
