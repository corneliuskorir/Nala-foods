from .interface.repository_interface import RepositoryInterface
from data import inventory


class InventoryRepository(RepositoryInterface):

    def __init__(self):
        pass

    def get(self):
        return inventory["products"]

    def add(self, data):
        return inventory["products"].append(data)

    def get_item(self, id):
        return next((item for item in inventory["products"] if item["id"] == id), None)

    def update(self, id, data):
        item = self.get_item(id)
        inventory["products"] = [
            item for item in inventory["products"] if item["id"] != id
        ]
        item |= data
        inventory["products"].append(item)
        return item

    def delete(self, id):
        inventory["products"] = [
            item for item in inventory["products"] if item["id"] != id
        ]
        return True
