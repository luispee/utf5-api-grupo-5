from fastapi import FastAPI
from app.api.routers import orders, products

app = FastAPI(
    title="API Integral para Punto de Venta (Food Truck)",
    description="Puerta de entrada HTTP optimizada para la interfaz concurrente del Cajero.",
    version="1.1.0"
)

# Registrar los routers de la API
app.include_router(orders.router)
app.include_router(products.router)

@app.get("/", include_in_schema=False)
async def root():
    return {"status": "API Operativa"}
