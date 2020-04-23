""" Defines the Order commands """

from models import Order


class OrderCommands:
    """ The commands for the order model """

    @staticmethod
    def get(order_id=None):
        """ Query an order by order_id """
        if order_id:
            return Order.query.filter_by(order_id=order_id).one()
        return Order.query.all()

    @staticmethod
    def create(order_id, items=None, delivery=None, total_price=None):
        """ Create a new order """
        order = Order(order_id, items=items, delivery=delivery, total_price=total_price)
        return order.save()

    def update(self, order_id, items=None, delivery=None, total_price=None):
        """ Update an order """
        order = self.get(order_id)
        if items:
            order.items = items
        if delivery:
            order.delivery = delivery
        if total_price:
            order.total_price = total_price
        return order.save()

    @staticmethod
    def delete(order_id):
        """ Delete an order """
        order = Order.query.filter_by(order_id=order_id).one()
        return order.delete()
