from flask import Blueprint
from flask_restx import Api

blueprint = Blueprint("api", __name__)
authorizations = {"apikey": {"type": "apiKey", "in": "header", "name": "Authorization"}}
api = Api(
    blueprint,
    title="FLASK RESTPLUS(RESTX) API BOILER-PLATE WITH JWT",
    version="1.0",
    description="a boilerplate for flask restplus (restx) web service",
    authorizations=authorizations,
    security="apikey",
)