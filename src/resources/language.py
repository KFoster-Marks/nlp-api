"""
Define the REST verbs relative to language utils
"""

from flasgger import swag_from
from flask.json import jsonify
from flask_restful import Resource
from flask_restful.reqparse import Argument

# from repositories import UserRepository
from util import parse_params


class LanguageResource(Resource):
    """ Verbs relative to the language utils """

    @staticmethod
    # @swag_from("../swagger/user/GET.yml")
    def get(method):
        """ Return language information requested """
        print('This is the method: ', method)
        response = 'This is where you will do the coolest stuff Kristen!'
        return jsonify({ "message": response })

    # @staticmethod
    # @parse_params(
    #     Argument("age", location="json", required=True, help="The age of the user.")
    # )
    # @swag_from("../swagger/user/POST.yml")
    # def post(last_name, first_name, age):
    #     """ Create an user based on the sent information """
    #     user = UserRepository.create(
    #         last_name=last_name, first_name=first_name, age=age
    #     )
    #     return jsonify({"user": user.json})
    #
    # @staticmethod
    # @parse_params(
    #     Argument("age", location="json", required=True, help="The age of the user.")
    # )
    # @swag_from("../swagger/user/PUT.yml")
    # def put(last_name, first_name, age):
    #     """ Update an user based on the sent information """
    #     repository = UserRepository()
    #     user = repository.update(last_name=last_name, first_name=first_name, age=age)
    #     return jsonify({"user": user.json})
