from datetime import datetime, timezone
class OrderRepository:
    def __init__(self):
        self.orders = []

    def save(self, order):
        order["updatedAt"] = datetime.now(timezone.utc)
        self.orders.append(order)
        return order

    def get_all(self):
        return self.orders

    def get_active_orders(self):
        return [
            order for order in self.orders
            if order["status"] != "ENTREGADO"
        ]


order_repository = OrderRepository()