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
