from .interface.inventory_service_interface import InventoryInterface
from repository.inventory_service import InventoryRepository
from models.product import Product


class InventoryService(InventoryInterface):
    def __init__(self, repository: InventoryRepository):
        self._repo = repository

    def get(self):
        return self._repo.get()

    def add(self, data):
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
        return self._repo.update(id=id, data=data)

    def delete(self, id):
        return self._repo.delete(id)
