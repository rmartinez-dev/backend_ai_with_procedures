from app.repositories.product_repository import get_products_repository, create_product_repository, delete_product_repository, update_product_repository, get_products_by_id_repository
from app.schemas.product_schema import ProductSchema

def get_products_controller():
    products = get_products_repository()
    return products

def create_product_controller(product: ProductSchema):
    create_product_repository(product)

def delete_product_controller(id: int):
    delete_product_repository(id)

def update_product_controller(product: ProductSchema):
    update_product_repository(product)

def get_products_by_id_controller(id: int):
    products = get_products_by_id_repository(id)
    return products