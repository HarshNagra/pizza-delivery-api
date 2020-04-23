import json
import unittest
import unittest.mock as mock


from models import Order
from models.abc import db
from PizzaParlour import app
from commands import ItemCommands
from mock_data import MOCK_ITEMS


class TestDelivery(unittest.TestCase):
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

    def test_create(self):
        """ The POST on `/delivery` should create a order """
        order_details = [{"name": MOCK_ITEMS[0]['name']}]
        service = "UberEats"
        address = "123 Queen St., Toronto, ON"
        service_order_id = "UberEats_1234"

        response = self.client.post(
            "/v1/delivery",
            content_type="application/json",
            data=json.dumps({"order_details": order_details, "service": service,
                             "address": address, "service_order_id": service_order_id}),
        )

        expected = {
            "delivery": {
                "order_id": mock.ANY,
                "items": [{**MOCK_ITEMS[0], "item_id": mock.ANY}],
                "total_price": MOCK_ITEMS[0]['price'],
                "delivery": {
                    "service": service,
                    "address": address,
                    "service_order_id": service_order_id
                }
            }
        }
        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.data.decode("utf-8"))
        self.assertEqual(
            response_json,
            expected,
        )
        self.assertEqual(Order.query.count(), 1)
