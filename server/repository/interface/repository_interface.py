from abc import ABC, abstractmethod


class RepositoryInterface(ABC):

    @abstractmethod
    def get(self):
        """get all items"""

    @abstractmethod
    def add(self, data):
        """add items"""

    @abstractmethod
    def get_item(self, id):
        """get item"""

    @abstractmethod
    def update(self, id, data):
        """update item"""

    @abstractmethod
    def delete(self, id):
        """delete item"""
