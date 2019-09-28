"""
Defines the blueprint for language utils
"""
from flask import Blueprint
from flask_restful import Api

from resources import LanguageResource

LANGUAGE_BLUEPRINT = Blueprint("language", __name__)
Api(LANGUAGE_BLUEPRINT).add_resource(
    LanguageResource, "/language/<string:method>"
)
