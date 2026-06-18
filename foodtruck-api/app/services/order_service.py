from decimal import Decimal
from uuid import uuid4

from app.repositories.product_repository import product_repository
from app.repositories.order_repository import order_repository


class OrderService:

    def calcular_totales(self, payload):
        subtotal = Decimal("0.00")

        for item in payload.items:
            product = product_repository.get_by_id(item.productId)

            if not product:
                raise Exception(f"Producto {item.productId} no existe")

            if not product["isAvailable"]:
                raise Exception(f"Producto sin stock")

            subtotal += product["price"] * item.quantity

        tax = Decimal("0.00")
        total = subtotal + tax

        return {
            "subtotal": subtotal,
            "tax": tax,
            "total": total
        }

    def registrar_orden(self, payload):
        totals = self.calcular_totales(payload)

        nueva_orden = {
            "orderId": uuid4(),
            "customerName": payload.customerName,
            "status": "PREPARANDO",
            "totalAmount": totals["total"]
        }

        return order_repository.save(nueva_orden)

    def listar_pedidos_activos(self):
        return order_repository.get_active_orders()


order_service = OrderService()