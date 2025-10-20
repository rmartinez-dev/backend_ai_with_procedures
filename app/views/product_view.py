from fastapi import APIRouter, HTTPException
from ..controllers.product_controller import create_product_controller, delete_product_controller, get_products_by_id_controller, get_products_controller, update_product_controller
from app.schemas.product_schema import ProductSchema

router = APIRouter(prefix="/products", tags=["products"])

@router.get("/")
def get_products_views():
    try:
        return get_products_controller()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/")
def create_client_view(product: ProductSchema):
    try:
        return create_product_controller(product)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{product_id}")
def delete_product_view(product_id: int):
    try:
        return delete_product_controller(product_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{product_id}")
def get_products_by_id_view(product_id: int):
    try:
        return get_products_by_id_controller(product_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/")
def update_product_view(product: ProductSchema):
    try:
        return update_product_controller(product)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
