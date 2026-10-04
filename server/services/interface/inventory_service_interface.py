from abc import ABC, abstractmethod


class InventoryInterface(ABC):

    @abstractmethod
    def get(self):
        """get all items"""

    @abstractmethod
    def add(self, data):
        """add item"""

    @abstractmethod
    def get_item(self, id):
        """get item by id"""

    @abstractmethod
    def update(self, id, data):
        """update item"""

    @abstractmethod
    def delete(self, id):
        """delete items"""
