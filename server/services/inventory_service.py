from .interface.inventory_service_interface import InventoryInterface
from repository import InventoryRepository
from models.product import Product


class InventoryService(InventoryInterface):
    def __init__(self, repository: InventoryRepository):
        self._repo = repository

    def get(self):
        return self._repo.get()

    def add(self, data):
        new_id = max((item["id"] for item in self.get()), default=0) + 1
        data["id"] = new_id
        product = Product(**data)
        return self._repo.add(data=product.to_dict())

    def get_item(self, id):
        item = self._repo.get_item(id)
        if item:
            product = Product(**item)
            return product.to_dict()
        return None

    def update(self, id, data):
        if not data:
            return None
        item = self.get_item(id)
        item |= data
        prod = Product(**item)

        return self._repo.update(id=prod.id, data=prod.to_dict())

    def delete(self, id):
        return self._repo.delete(id)
