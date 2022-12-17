"""
Schemas for all application models.
"""
from marshmallow import Schema, fields, pre_load, validate


class UserSchema(Schema):
    """
    Schemas for User model
    """
    username = fields.Str(validate=validate.Length(min=1))
    password = fields.Str(validate=validate.Length(min=1))

    @pre_load
    def process_input(self, data, **kwargs):
        """
        Pre-processing the username and password to strip extra whitespaces
        Args:
            data(dict): data provided by user.

        Returns: dict
        """
        data['username'] = data.get('username', '').strip()
        data['password'] = data.get('password', '').strip()
        return data


class BookSchema(Schema):
    """
    Schemas for Book model
    """
    title = fields.Str(validate=validate.Length(min=1))
    description = fields.Str(validate=validate.Length(min=1))
    pages = fields.Integer(
        strict=True, required=True, validate=[validate.Range(min=1, error="Value must be greater than 0")]
    )
    published_on = fields.DateTime(required=True, format='%Y-%m-%d')

    @pre_load
    def process_input(self, data, **kwargs):
        """
        Pre-processing the title and description to strip extra whitespaces
        Args:
            data(dict): data provided by user.

        Returns: dict
        """
        data['title'] = data.get('title', '').strip()
        data['description'] = data.get('description', '').strip()
        return data
