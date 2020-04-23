"""
Defines the blueprint for the item
"""
from flask import Blueprint
from flask_restful import Api

from resources import ItemResource

ITEM_BLUEPRINT = Blueprint("item", __name__)
Api(ITEM_BLUEPRINT).add_resource(
    ItemResource,
    "/menu",
    "/menu/<string:name>",
    "/menu/<string:name>/<string:size>",
)
