from .interface.repository_interface import RepositoryInterface


class InventoryRepository(RepositoryInterface):

    def __init__(self, inventory: dict):
        self.inventory: dict = inventory

    def get(self):
        return self.inventory["products"]

    def add(self, data):
        self.inventory["products"].append(data)
        return data

    def get_item(self, id):
        return next(
            (item for item in self.inventory["products"] if item["id"] == id), None
        )

    def update(self, id, data):
        item = self.get_item(id)
        self.inventory["products"] = [
            item for item in self.inventory["products"] if item["id"] != id
        ]
        item |= data
        self.inventory["products"].append(item)
        return item

    def delete(self, id):
        self.inventory["products"] = [
            item for item in self.inventory["products"] if item["id"] != id
        ]
        return True
