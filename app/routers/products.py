from fastapi import APIRouter, status

router = APIRouter(prefix="/api/v1/products", tags=["Products"])

@router.get("/", status_code=status.HTTP_501_NOT_IMPLEMENTED)
def list_products():
    return {"detail": "Not implemented"}

@router.post("/", status_code=status.HTTP_501_NOT_IMPLEMENTED)
def create_product():
    return {"detail": "Not implemented"}

@router.get("/{product_id}", status_code=status.HTTP_501_NOT_IMPLEMENTED)
def get_product(product_id: str):
    return {"detail": "Not implemented"}

@router.put("/{product_id}", status_code=status.HTTP_501_NOT_IMPLEMENTED)
def update_product(product_id: str):
    return {"detail": "Not implemented"}

@router.delete("/{product_id}", status_code=status.HTTP_501_NOT_IMPLEMENTED)
def delete_product(product_id: str):
    return {"detail": "Not implemented"}