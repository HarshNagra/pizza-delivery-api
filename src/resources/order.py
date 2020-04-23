"""
Define the REST verbs relative to the orders
"""

from flask.json import jsonify
from flask import request
from flask_restful import Resource
import shortuuid

from commands import (
    OrderCommands,
    ItemCommands,
)


class OrderResource(Resource):
    """ Verbs relative to the order """
    def _get_items_data(items=[]):
        """ Return full items data with prices, sizes,
        categories from their names and sizes """
        item_commands = ItemCommands()
        return item_commands.get_all(items)

    def _get_total_price(items=[]):
        """ Calculate total price from list of items """
        return sum([item['price'] for item in items])

    @staticmethod
    def get(order_id=None):
        """ Return order information based on order_id """
        if order_id:
            order = OrderCommands.get(order_id=order_id)
            return jsonify({"order": order.json})
        else:
            orders = OrderCommands.get(order_id=order_id)
            return jsonify({"orders": [order.json for order in orders]})

    @staticmethod
    def post():
        """ Create an order based on the sent information """
        json_data = request.get_json(force=True)
        order_id = f"order_{shortuuid.uuid()}"
        items = OrderResource._get_items_data(
            items=json_data.get('items', []),
        )
        total_price = OrderResource._get_total_price(items=items)
        order = OrderCommands.create(
            order_id=order_id,
            items=items,
            delivery=json_data.get('delivery', None),
            total_price=total_price,
        )
        return jsonify({"order": order.json})

    @staticmethod
    def put(order_id):
        """ Update an order based on the sent information """
        if not order_id:
            return "Must specify an order_id"
        json_data = request.get_json(force=True)
        items = OrderResource._get_items_data(
            items=json_data.get('items', [])
        )
        total_price = OrderResource._get_total_price(items=items)
        repository = OrderCommands()
        order = repository.update(
            order_id=order_id,
            items=items,
            delivery=json_data.get('delivery', None),
            total_price=total_price
        )
        return jsonify({"order": order.json})

    @staticmethod
    def delete(order_id=None):
        """ Delte an order by order_id """
        if not order_id:
            return "Must specify an order_id"
        repository = OrderCommands()
        repository.delete(order_id=order_id)
        return {"order": {"order_id": order_id}}
