from pydantic import BaseModel, Field
from typing import List
from enum import Enum
from uuid import UUID
from decimal import Decimal
from datetime import datetime

class EstadoPedidoEnum(str, Enum):
    PREPARANDO = "PREPARANDO"
    LISTO = "LISTO"
    ENTREGADO = "ENTREGADO"

class OrderItemBase(BaseModel):
    productId: UUID = Field(..., example="123e4567-e89b-12d3-a456-426614174000")
    quantity: int = Field(..., ge=1, example=2)

class OrderCreateRequest(BaseModel):
    customerName: str = Field(..., min_length=1, example="Juan Pérez")
    items: List[OrderItemBase]

class OrderCalculationRequest(BaseModel):
    items: List[OrderItemBase]

class OrderCalculationResponse(BaseModel):
    subtotal: Decimal = Field(..., example=17.00)
    tax: Decimal = Field(..., example=0.00)
    total: Decimal = Field(..., example=17.00)

class OrderResponse(BaseModel):
    orderId: UUID
    customerName: str
    status: str
    totalAmount: Decimal

class OrderDashboardItem(BaseModel):
    orderId: UUID
    customerName: str
    status: EstadoPedidoEnum
    updatedAt: datetime
