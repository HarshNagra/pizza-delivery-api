import json
import unittest
import unittest.mock as mock


from models import Order
from models.abc import db
from commands import (
    OrderCommands,
    ItemCommands,
)
from PizzaParlour import app
from mock_data import (
    MOCK_ITEMS,
    MOCK_ORDER_REQUEST,
    MOCK_ORDER_RESPONSE,
)


class TestOrder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

    def setUp(self):
        db.create_all()
        for item in MOCK_ITEMS:
            ItemCommands.create(**item)

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get(self):
        """ The GET on `/order/:order_id` should return an order """
        order_id = "order_1"
        mock_order = {
            **MOCK_ORDER_RESPONSE[0],
            "order_id": order_id,
        }
        OrderCommands.create(**mock_order)

        response = self.client.get(f"/v1/order/{order_id}")
        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.data.decode("utf-8"))
        self.assertEqual(
            response_json,
            {"order": mock_order},
        )

    def test_get_all(self):
        """ The GET on `/order` should return all orders """
        mock_orders = [
            {**mock_order, "order_id": f"order_{i}"}
            for i, mock_order in enumerate(MOCK_ORDER_RESPONSE)
        ]

        for mock_order in mock_orders:
            OrderCommands.create(**mock_order)

        response = self.client.get(f"/v1/order")
        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.data.decode("utf-8"))
        self.assertEqual(
            response_json,
            {"orders": MOCK_ORDER_RESPONSE},
        )

    def test_create(self):
        """ The POST on `/order` should create an order """
        response = self.client.post(
            "/v1/order",
            content_type="application/json",
            data=json.dumps(MOCK_ORDER_REQUEST[0]),
        )

        expected_response = {
            "order": {
                **MOCK_ORDER_RESPONSE[0],
                "items": [
                    {**mock_item, "item_id": mock.ANY}
                    for mock_item in MOCK_ORDER_RESPONSE[0]['items']
                ]
            }
        }

        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.data.decode("utf-8"))
        self.assertEqual(
            response_json,
            expected_response,
        )
        self.assertEqual(Order.query.count(), 1)

    def test_update(self):
        """ The PUT on `/order` should update an order """
        order_id = "order_1"
        mock_order = {
            **MOCK_ORDER_RESPONSE[0],
            "order_id": order_id,
        }
        OrderCommands.create(**mock_order)

        mock_updated_items_request = MOCK_ORDER_REQUEST[1]['items']
        mock_updated_items_response = [{
            **MOCK_ITEMS[1],
            "item_id": 2,
        }]
        response = self.client.put(
            f"/v1/order/{order_id}",
            content_type="application/json",
            data=json.dumps({"items": mock_updated_items_request}),
        )

        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.data.decode("utf-8"))
        expected_response = {
            "order": {
                **mock_order,
                "items": mock_updated_items_response,
                "total_price": MOCK_ITEMS[1]['price'],
            }
        }
        self.assertEqual(
            response_json,
            expected_response,
        )
        order = OrderCommands.get(order_id=order_id)
        self.assertEqual(order.items, mock_updated_items_response)

    def test_delete(self):
        """ The DELETE on `/order` should delete an order """
        order_id = "order_3"
        items = [{"name": "Pepsi", "price": 10.00}]
        delivery = {"service": "UberEats"}
        OrderCommands.create(order_id=order_id, items=items, delivery=delivery)
        response = self.client.delete(
            f"/v1/order/{order_id}",
        )
        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.data.decode("utf-8"))
        self.assertEqual(
            response_json,
            {"order": {"order_id": order_id}},
        )
        try:
            OrderCommands.get(order_id=order_id)
        except Exception as e:
            self.assertEqual(str(e), 'No row was found for one()')
