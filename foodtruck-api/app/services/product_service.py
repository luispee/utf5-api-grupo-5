from app.repositories.product_repository import product_repository


class ProductService:

   def obtener_catalogo(self):
        products = product_repository.products

        return [
            {
                "id": product_id,
                **product
            }
            for product_id, product in products.items()
        ]


product_service = ProductService()