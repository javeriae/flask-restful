"""
Helper methods for application
"""
import json

from app.app import fernet


def encrypt(data):
    """
    Method to encrypt the data for security.
    Args:
        data(dict): data to encrypt

    Returns: string

    """
    plain_text = json.dumps(data)
    encrypted_text = fernet.encrypt(plain_text.encode())
    return encrypted_text.decode()


def decrypt(encrypted_text):
    """
    Method to decrypted the encrypted text to plain text.
    Args:
        encrypted_text(string):

    Returns: dict

    """
    plain_text = fernet.decrypt(encrypted_text.encode()).decode()
    data = json.loads(plain_text)
    return data
