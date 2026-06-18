from fastapi import APIRouter, status
from typing import List
from app.api.schemas.products import ProductResponse
from app.services.product_service import product_service

router = APIRouter(prefix="/products", tags=["Catálogo"])

@router.get("/", response_model=List[ProductResponse], status_code=status.HTTP_200_OK)
async def obtener_catalogo():
    """
    **Obtener catálogo de productos disponibles.**
    Garantiza la visibilidad del estado del sistema al cajero mostrando los ítems en stock.
    """
    # Hardcodeamos datos de prueba basados en el ItemMenu del dominio
    return product_service.obtener_catalogo()
    
