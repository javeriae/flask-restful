"""
Routes for all application views.
"""
from flask import Blueprint
from flask_restful import Api

from .views import Index, UserItems

home_bp = Blueprint('home_bp', __name__)

home_api = Api(home_bp)

home_api.add_resource(Index, '/')
home_api.add_resource(UserItems, '/users')
