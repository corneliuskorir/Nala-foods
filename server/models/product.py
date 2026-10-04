class Product:
    def __init__(self, id, name, quantity=0, brands=[]):
        self._id = id
        self.name = name
        self._quantity = quantity
        self.brands = brands

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        raise PermissionError("Immutable property id cannot be changed")

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError(f"Invalid quantity: {value}")
        self._quantity = value

    def add_brand(self, brand):
        if not brand and not isinstance(brand, str):
            raise ValueError("Invalid brand")
        self.brands.append(brand)

    def to_dict(self):
        return {
            "id": self._id,
            "name": self.name,
            "quantity": self._quantity,
            "brands": self.brands,
        }
