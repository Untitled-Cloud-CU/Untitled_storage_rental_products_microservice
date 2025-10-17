from fastapi import FastAPI
from app.routers import products, orders

app = FastAPI(title="Products/Orders Service", version="1.0.0")

app.include_router(products.router)
app.include_router(orders.router)

@app.get("/health")
def health():
    return {"status": "ok", "service": "products-orders-v2"}