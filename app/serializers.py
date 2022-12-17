"""
Serializers for all application model.
"""

def user_serializer(user):
    """
    Serialize the fields of user.

    Arguments:
        user: User object
    """
    return {
        'username': user.username,
        'password': user.password
    }
