""" Defines the Item commands """

from models import Item


class ItemCommands:
    """ The commands for the order model """

    @staticmethod
    def get(name=None, size=None):
        """ Query an item by name and size """
        if not name and not size:
            return Item.query.all()
        if name and size:
            return Item.query.filter_by(name=name.lower()).filter_by(size=size)
        if name:
            return Item.query.filter_by(name=name.lower())

    @staticmethod
    def create(name, size, price, category):
        """ Create a new item """
        item = Item(name=name, size=size, price=price, category=category)
        return item.save()

    def get_all(self, items):
        """ Query a list of items by name and size """
        return [
            self.get(
                name=item['name'],
                size=item.get('size', None),
            ).one().json
            for item in items
        ]
