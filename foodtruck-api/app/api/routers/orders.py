from fastapi import APIRouter, status, Path, Body
from typing import List
from uuid import UUID
from app.api.schemas.orders import (
    OrderCreateRequest, 
    OrderResponse, 
    OrderCalculationRequest, 
    OrderCalculationResponse,
    OrderDashboardItem,
    EstadoPedidoEnum
)

router = APIRouter(prefix="/orders", tags=["Gestión de Órdenes"])

@router.post("/", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
async def registrar_orden(payload: OrderCreateRequest):
    """
    **UC02: Registrar y Confirmar Orden (Ingresar Orden).**
    Crea la orden final en el sistema tras la confirmación del cajero.
    """
    # Aquí se invocará a pedido_service.crearPedido() más adelante
    return {
        "orderId": "123e4567-e89b-12d3-a456-426614174001",
        "customerName": payload.customerName,
        "status": "PREPARANDO",
        "totalAmount": 17.00
    }

@router.post("/calculate-totals", response_model=OrderCalculationResponse)
async def calcular_totales(payload: OrderCalculationRequest):
    """
    **Evitar Errores de Cálculo:**
    Permite al frontend enviar el carrito actual para retornar subtotales calculados en el backend.
    """
    return {"subtotal": 17.00, "tax": 0.00, "total": 17.00}

@router.get("/active-board", response_model=List[OrderDashboardItem])
async def listar_pedidos_activos():
    """
    **Eficiencia y Anticipación:**
    Retorna en una sola consulta los pedidos en preparación y LISTOS para el tablero del cajero.
    """
    return [
        {
            "orderId": "123e4567-e89b-12d3-a456-426614174001",
            "customerName": "Ana Gómez",
            "status": EstadoPedidoEnum.LISTO,
            "updatedAt": "2026-06-15T15:30:00Z"
        }
    ]

@router.patch("/{orderId}/status", response_model=dict)
async def cambiar_estado_pedido(
    orderId: UUID = Path(...),
    status: EstadoPedidoEnum = Body(..., embed=True)
):
    """
    **Ley de Fitts / Cambio de Estado Concurrente:**
    Modifica el estado a LISTO (alerta pantalla) o ENTREGADO (retiro físico) en un solo toque.
    """
    return {"message": f"Pedido {orderId} actualizado a {status.value} exitosamente."}
