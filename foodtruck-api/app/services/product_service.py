from app.repositories.product_repository import product_repository


class ProductService:

    def obtener_catalogo(self):
        return product_repository.get_all()


product_service = ProductService()