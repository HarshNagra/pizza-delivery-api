import unittest.mock as mock

MOCK_ITEMS = [
    {"name": "pepsi", "size": "m", "price": 3.50, "category": "drink"},
    {"name": "coke", "size": "m", "price": 3.00, "category": "drink"},
]


MOCK_ORDER_REQUEST = [
    {
        "items": [{"name": "pepsi", "size": "m"}],
        "delivery": {"service": "UberEats"},
    },
    {
        "items": [{"name": "coke", "size": "m"}],
        "delivery": {"service": "Foodora"},
    },
]

MOCK_ORDER_RESPONSE = [
    {
        "order_id": mock.ANY,
        "items": [MOCK_ITEMS[0]],
        "total_price": MOCK_ITEMS[0]["price"],
        "delivery": {"service": "UberEats"},
    },
    {
        "order_id": mock.ANY,
        "items": [MOCK_ITEMS[1]],
        "total_price": MOCK_ITEMS[1]["price"],
        "delivery": {"service": "Foodora"},
    },
]
