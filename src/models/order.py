"""
Define the User model
"""
from .sql import db
from .abc import BaseModel, MetaBaseModel


class Order(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The Order model """

    __tablename__ = "order"

    order_id = db.Column(db.String(300), primary_key=True)
    items = db.Column(db.JSON, nullable=False)
    delivery = db.Column(db.JSON, nullable=True)
    total_price = db.Column(db.Float, nullable=True)

    def __init__(self, order_id, items, delivery=None, total_price=None):
        """ Create a new Order """
        self.order_id = order_id
        self.items = items
        self.delivery = delivery
        self.total_price = total_price
