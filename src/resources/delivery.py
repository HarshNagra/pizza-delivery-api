"""
Define the REST verbs relative to the delivery
"""

from flask.json import jsonify
from flask_restful import Resource
from flask import request
import shortuuid

from commands import (
    ItemCommands,
    OrderCommands,
)


class DeliveryResource(Resource):
    """ Verbs relative to the delivery """
    def _get_items_data(items=[]):
        """ Return full items data with prices, sizes,
        categories from their names and sizes """
        item_commands = ItemCommands()
        return item_commands.get_all(items)

    def _get_total_price(items=[]):
        """ Calculate total price from list of items """
        return sum([item['price'] for item in items])

    @staticmethod
    def post():
        """ Create an order based on the sent delivery information """
        json_data = request.get_json(force=True)
        order_id = f"order_{shortuuid.uuid()}"
        items = DeliveryResource._get_items_data(items=json_data.get('order_details', []))
        total_price = DeliveryResource._get_total_price(items=items)
        delivery = OrderCommands.create(
            order_id=order_id,
            items=items,
            total_price=total_price,
            delivery={
                "service": json_data.get('service', None),
                "address": json_data.get('address', None),
                "service_order_id": json_data.get('service_order_id', None),
            }
        )
        return jsonify({"delivery": delivery.json})
