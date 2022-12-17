"""
Constants for application.
"""
from app.helpers import encrypt

RESOURCE_NOT_FOUND = encrypt({
        'error_msg': 'Resource not found.',
        'error_code': 'NOT_FOUND',
        'status_code': 404
    }), 404

INVALID_DATA = encrypt({
        'error_msg': 'Invalid data.',
        'error_code': 'BAD_REQUEST',
        'status_code': 400
    }), 400
