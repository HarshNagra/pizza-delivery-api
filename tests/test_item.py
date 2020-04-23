import json
import unittest
import unittest.mock as mock

from models.abc import db
from commands import ItemCommands
from PizzaParlour import app
from mock_data import (
    MOCK_ITEMS,
)


class TestItem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_all(self):
        """ The GET on `/menu` should return all items"""
        for mock_item in MOCK_ITEMS:
            ItemCommands.create(**mock_item)

        response = self.client.get(f"/v1/menu")
        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.data.decode("utf-8"))
        self.assertEqual(
            response_json,
            {"items": [{**item, "item_id": mock.ANY} for item in MOCK_ITEMS]},
        )

    def test_get_name(self):
        """ The GET on `/menu/:name` should only return items with matching name"""

        for mock_item in MOCK_ITEMS:
            ItemCommands.create(**mock_item)

        response = self.client.get(f"/v1/menu/{MOCK_ITEMS[0]['name']}")
        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.data.decode("utf-8"))
        self.assertEqual(
            response_json,
            {"items": [{**MOCK_ITEMS[0], "item_id": mock.ANY}]},
        )
