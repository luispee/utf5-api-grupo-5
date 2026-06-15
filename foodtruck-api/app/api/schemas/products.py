from pydantic import BaseModel, Field
from uuid import UUID
from decimal import Decimal

class ProductResponse(BaseModel):
    id: UUID = Field(..., example="123e4567-e89b-12d3-a456-426614174000")
    name: str = Field(..., example="Hamburguesa Completa")
    description: str = Field(..., example="Carne, queso, lechuga, tomate y salsa de la casa")
    price: Decimal = Field(..., example=8.50)
    isAvailable: bool = Field(..., example=True)
