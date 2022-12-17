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


def book_serializer(book):
    """
    Serialize the fields of book.

    Arguments:
        book: Book object
    """
    return {
        'title': book.title,
        'description': book.description,
        'pages': book.pages,
        'published_on': book.published_on.strftime('%Y-%m-%d')
    }
