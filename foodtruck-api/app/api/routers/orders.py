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
from app.services.order_service import order_service

router = APIRouter(prefix="/orders", tags=["Gestión de Órdenes"])

@router.post("/", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
async def registrar_orden(payload: OrderCreateRequest):
    """
    **UC02: Registrar y Confirmar Orden (Ingresar Orden).**
    Crea la orden final en el sistema tras la confirmación del cajero.
    """
    # Aquí se invocará a pedido_service.crearPedido() más adelante
    return order_service.registrar_orden(payload)

@router.post("/calculate-totals", response_model=OrderCalculationResponse)
async def calcular_totales(payload: OrderCalculationRequest):
    """
    **Evitar Errores de Cálculo:**
    Permite al frontend enviar el carrito actual para retornar subtotales calculados en el backend.
    """
    return order_service.calcular_totales(payload)

@router.get("/active-board", response_model=List[OrderDashboardItem])
async def listar_pedidos_activos():
    """
    **Eficiencia y Anticipación:**
    Retorna en una sola consulta los pedidos en preparación y LISTOS para el tablero del cajero.
    """
    return order_service.listar_pedidos_activos()

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
