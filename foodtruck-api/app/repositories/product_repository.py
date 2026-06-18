from decimal import Decimal


class ProductRepository:
    def __init__(self):
        self.products = {
            "123e4567-e89b-12d3-a456-426614174000": {
                "name": "Hamburguesa Completa",
                "price": Decimal("8.50"),
                "isAvailable": True
            },
            "c9a646d3-9c61-4cd8-8936-795323214561": {
                "name": "Papas Fritas Grandes",
                "price": Decimal("4.00"),
                "isAvailable": True
            },
            "b3d11a22-4455-6677-8899-aabbccddeeff": {
                "name": "Refresco 500ml",
                "price": Decimal("2.50"),
                "isAvailable": False
            }
        }

    def get_by_id(self, product_id):
        return self.products.get(str(product_id))


product_repository = ProductRepository()