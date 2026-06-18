import json
from pathlib import Path
from datetime import datetime, timezone


class OrderRepository:
    def __init__(self):
        self.path = Path("app/data/orders.json")

    def save(self, order):
        order["updatedAt"] = datetime.now(timezone.utc).isoformat()

        with open(self.path, "r", encoding="utf-8") as file:
            orders = json.load(file)

        order["orderId"] = str(order["orderId"])
        order["totalAmount"] = float(order["totalAmount"])

        orders.append(order)

        with open(self.path, "w", encoding="utf-8") as file:
            json.dump(orders, file, indent=4)

        return order

    def get_all(self):
        with open(self.path, "r", encoding="utf-8") as file:
            return json.load(file)

    def get_active_orders(self):
        orders = self.get_all()

        return [
            order for order in orders
            if order["status"] != "ENTREGADO"
        ]


order_repository = OrderRepository()