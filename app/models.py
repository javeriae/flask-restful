"""
Application Models.
"""
from .app import db


class User(db.Model):  # pylint: disable=too-few-public-methods
    """
    User model for authentication.
    """
    __tablename__ = 'user'

    username = db.Column(db.String(128), primary_key=True)
    password = db.Column(db.String(128), nullable=False)

    def __str__(self):
        return f'{self.username}'
