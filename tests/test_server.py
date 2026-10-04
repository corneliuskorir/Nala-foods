from server import create_app, Product, inventory

import pytest

app = create_app()


@pytest.fixture(autouse=True)
def clear_data():
    inventory["products"].clear()
    yield
    inventory["products"].clear()


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


class TestServer:
    def test_index_route(self):
        client = app.test_client()
        res = client.get("/")
        assert "message" in res.get_json()
        assert res.status_code == 200

    def test_get_inventory_route(self, client):
        res = client.get("/inventory")
        assert res.status_code == 200

    def test_post_inventory_route(self, client):
        res = client.post("/inventory", json={"name": "test"})
        assert res.status_code == 201

        res = client.get("/inventory/1")
        data = res.get_json()
        assert data["name"] == "test"
        assert data["id"] == 1

    def test_get_invetory_item_route(self, client):
        res = client.post("/inventory", json={"name": "test"})
        assert res.status_code == 201

        res = client.get("/inventory/1")
        assert res.status_code == 200

        data = res.get_json()
        assert data["name"] == "test"
        assert data["id"] == 1

    def test_patch_invetory_item_route(self, client):
        res = client.post("/inventory", json={"name": "test"})
        assert res.status_code == 201

        res = client.patch("/inventory/1", json={"name": "changed"})
        data = res.get_json()
        assert data["name"] == "changed"
        assert res.status_code == 201

    def test_delete_invetory_item_route(self, client):
        res = client.delete("/inventory/1")
        assert res.status_code == 204


# model


class TestModel:
    def test_product_obj(self):
        new_product = Product(1, "test product", quantity=10, brands=["testbrand"])
        assert new_product.id == 1
        assert new_product.name == "test product"
        assert new_product.quantity == 10
        assert "testbrand" in new_product.brands

        new_product.add_brand("testbrand2")
        assert "testbrand2" in new_product.brands

    def test_obj_raise_errors(self):
        new_product = Product(1, "test product", quantity=10, brands=["testbrand"])
        with pytest.raises(PermissionError):
            new_product.id = 2

        with pytest.raises(ValueError):
            new_product.quantity = -1

        with pytest.raises(ValueError):
            new_product.add_brand(None)
