"""
Defines the blueprint for the delivery
"""
from flask import Blueprint
from flask_restful import Api

from resources import DeliveryResource

DELIVERY_BLUEPRINT = Blueprint("delivery", __name__)
Api(DELIVERY_BLUEPRINT).add_resource(
    DeliveryResource,
    "/delivery",
)
