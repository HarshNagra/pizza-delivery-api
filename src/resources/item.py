"""
Define the REST verbs relative to the items
"""

from flask.json import jsonify
from flask_restful import Resource

from commands import ItemCommands


class ItemResource(Resource):
    """ Verbs relative to the item """

    @staticmethod
    def get(name=None, size=None):
        """ Return item information based on name and size """
        items = ItemCommands.get(name=name, size=size)
        return jsonify({"items": [item.json for item in items]})
