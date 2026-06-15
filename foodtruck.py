from datetime import datetime
from decimal import Decimal
from enum import Enum
from typing import List, Optional
from uuid import UUID, uuid4

# ==========================================
# ENUMERACIONES (Enumeraciones)
# ==========================================

class EstadoPedido(Enum):
    PENDIENTE = "PENDIENTE"
    EN_PREPARACION = "EN_PREPARACION"
    LISTO = "LISTO"
    RETIRADO = "RETIRADO"
    CANCELADO = "CANCELADO"

class MetodoPago(Enum):
    TARJETA_CREDITO = "TARJETA_CREDITO"
    TARJETA_DEBITO = "TARJETA_DEBITO"
    MERCADO_PAGO = "MERCADO_PAGO"


# ==========================================
# ENTIDADES DEL DOMINIO
# ==========================================

class Cliente:
    def __init__(self, nombre: str, id: Optional[UUID] = None):
        self.id: UUID = id or uuid4()
        self.nombre: str = nombre

class FoodTruck:
    def __init__(self, nombre: str, ubicacion: str, activo: bool, id: Optional[UUID] = None):
        self.id: UUID = id or uuid4()
        self.nombre: str = nombre
        self.ubicacion: str = ubicacion
        self.activo: bool = activo

class ItemMenu:
    def __init__(self, nombre: str, descripcion: str, precio: Decimal, id: Optional[UUID] = None):
        self.id: UUID = id or uuid4()
        self.nombre: str = nombre
        self.descripcion: str = descripcion
        self.precio: Decimal = precio

class LineaDePedido:
    def __init__(self, cantidad: int, precioUnitario: Decimal, subtotal: Decimal, id: Optional[UUID] = None):
        self.id: UUID = id or uuid4()
        self.cantidad: int = cantidad
        self.precioUnitario: Decimal = precioUnitario
        self.subtotal: Decimal = subtotal

class Pago:
    def __init__(self, monto: Decimal, metodoPago: MetodoPago, estado: str, referencia: str, fecha: datetime, id: Optional[UUID] = None):
        self.id: UUID = id or uuid4()
        self.monto: Decimal = monto
        self.metodoPago: MetodoPago = metodoPago
        self.estado: str = estado
        self.referencia: str = referencia
        self.fecha: datetime = fecha

class Pedido:
    def __init__(self, numero: int, estado: EstadoPedido, total: Decimal, creadoEn: datetime, foodTruck: FoodTruck, id: Optional[UUID] = None):
        self.id: UUID = id or uuid4()
        self.numero: int = numero
        self.estado: EstadoPedido = estado
        self.total: Decimal = total
        self.creadoEn: datetime = creadoEn
        self.foodTruck: FoodTruck = foodTruck
        self.lineas: List[LineaDePedido] = []  # Relación 1..* con LineaDePedido
        self.pago: Optional[Pago] = None      # Relación 0..1 con Pago


# ==========================================
# REPOSITORIOS (Definiciones de Interfaz)
# ==========================================

class PedidoRepository:
    def save(self, p: Pedido) -> Pedido:
        raise NotImplementedError
        
    def findById(self, id: UUID) -> Optional[Pedido]:
        raise NotImplementedError
        
    def findByEstado(self, e: EstadoPedido) -> List[Pedido]:
        raise NotImplementedError
        
    def update(self, p: Pedido) -> Pedido:
        raise NotImplementedError

class ItemMenuRepository:
    def findAll(self) -> List[ItemMenu]:
        raise NotImplementedError
        
    def findById(self, id: UUID) -> Optional[ItemMenu]:
        raise NotImplementedError
        
    def save(self, i: ItemMenu) -> ItemMenu:
        raise NotImplementedError


# ==========================================
# SERVICIOS de la APLICACIÓN
# ==========================================

class PedidoService:
    def __init__(self, pedido_repo: PedidoRepository):
        self.pedido_repo = pedido_repo

    def crearPedido(self, dto) -> Pedido:
        """Satisface el caso de uso UC02: Tomar orden"""
        pass

    def actualizarEstado(self, id: UUID, e: EstadoPedido):
        """Satisface los cambios de estado eficientes del Cajero (UC08 / UC09)"""
        pass

    def obtenerCola(self) -> List[Pedido]:
        """Alimenta la pantalla del panel integrado del cajero (UC06)"""
        pass

    def calcularTotal(self, p: Pedido) -> Decimal:
        """Evita inconsistencias calculando de forma automatizada en el backend"""
        pass

class PagoService:
    def procesarPago(self, p: Pago) -> Pago:
        pass

    def confirmarPago(self, ref: str) -> bool:
        pass

    def reembolsar(self, id: UUID) -> None:
        pass

class NotificacionService:
    def notificarListoParaRetirar(self, p: Pedido) -> None:
        """Dispara las alertas en tiempo real en la pantalla pública"""
        pass
