"""
Defines the blueprint for the order
"""
from flask import Blueprint
from flask_restful import Api

from resources import OrderResource

ORDER_BLUEPRINT = Blueprint("order", __name__)
Api(ORDER_BLUEPRINT).add_resource(
    OrderResource,
    "/order",
    "/order/<string:order_id>",
)
