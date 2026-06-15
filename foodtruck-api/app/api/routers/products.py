from fastapi import APIRouter, status
from typing import List
from app.api.schemas.products import ProductResponse

router = APIRouter(prefix="/products", tags=["Catálogo"])

@router.get("/", response_model=List[ProductResponse], status_code=status.HTTP_200_OK)
async def obtener_catalogo():
    """
    **Obtener catálogo de productos disponibles.**
    Garantiza la visibilidad del estado del sistema al cajero mostrando los ítems en stock.
    """
    # Hardcodeamos datos de prueba basados en el ItemMenu del dominio
    return [
        {
            "id": "123e4567-e89b-12d3-a456-426614174000",
            "name": "Hamburguesa Completa",
            "description": "Carne, queso, lechuga, tomate y salsa de la casa",
            "price": 8.50,
            "isAvailable": True
        },
        {
            "id": "c9a646d3-9c61-4cd8-8936-795323214561",
            "name": "Papas Fritas Grandes",
            "description": "Porción individual de papas rústicas crujientes",
            "price": 4.00,
            "isAvailable": True
        },
        {
            "id": "b3d11a22-4455-6677-8899-aabbccddeeff",
            "name": "Refresco 500ml",
            "description": "Bebida cola fría",
            "price": 2.50,
            "isAvailable": False
        }
    ]
