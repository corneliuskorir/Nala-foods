from server import create_app, Product
import pytest

app = create_app()


class TestServer:
    def test_index_route(self):
        client = app.test_client()
        res = client.get("/")
        assert "message" in res.get_json()
        assert res.status_code == 200

    def test_get_invetory_route(self):
        client = app.test_client()
        res = client.get("/inventory")
        assert res.status_code == 200

    def test_post_invetory_route(self):
        client = app.test_client()
        res = client.post("/inventory")
        assert res.status_code == 201

    def test_get_invetory_item_route(self):
        client = app.test_client()
        res = client.get("/inventory/1")
        assert res.status_code == 200

    def test_patch_invetory_item_route(self):
        client = app.test_client()
        res = client.patch("/inventory/1")
        assert res.status_code == 201

    def test_delete_invetory_item_route(self):
        client = app.test_client()
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
