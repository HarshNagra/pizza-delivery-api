"""
Define the Item model
"""
from .sql import db
from .abc import BaseModel, MetaBaseModel


class Item(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The Item model """

    __tablename__ = "item"

    item_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), nullable=False)
    price = db.Column(db.Float, nullable=True)
    size = db.Column(db.String(300), nullable=True)
    category = db.Column(db.String(300), nullable=True)

    def __init__(self, name, price, size, category):
        """ Create a new Item """
        self.name = name
        self.price = price
        self.size = size
        self.category = category
