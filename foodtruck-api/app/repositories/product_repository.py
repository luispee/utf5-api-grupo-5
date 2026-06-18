import json
from pathlib import Path
from decimal import Decimal


class ProductRepository:
    def __init__(self):
        self.path = Path("app/data/products.json")

    def get_all(self):
        with open(self.path, "r", encoding="utf-8") as file:
            return json.load(file)

    def get_by_id(self, product_id):
        products = self.get_all()

        for product in products:
            if product["id"] == str(product_id):
                product["price"] = Decimal(str(product["price"]))
                return product

        return None


product_repository = ProductRepository()