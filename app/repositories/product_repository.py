from app.core.db import get_db_connection
from app.schemas.product_schema import ProductSchema
import psycopg2.extras


def get_products_repository():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("select * from product;")
    rows = cur.fetchall()
    cur.close()
    return rows

def create_product_repository(product: ProductSchema):
    conn = get_db_connection()
    cur = conn.cursor()

    arguments = (
        product.shopify_product_id,
        product.title,
        product.handle,
        product.status,
        product.vendor,
        product.product_type,
        product.created_at,
        product.updated_at,
        product.ingested_at
    )
    cur.execute(
            f"""INSERT INTO public.product(
                                           shopify_product_id, 
                                           title, 
                                           handle, 
                                           status, 
                                           vendor, 
                                           product_type, 
                                           created_at, 
                                           updated_at, 
                                           ingested_at)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);""", 
            arguments
            )
    conn.commit()
    cur.close
    return {"mensaje": "product creado", "product": product}

def update_product_repository(product: ProductSchema):
    conn = get_db_connection()
    cur = conn.cursor()

    arguments= (
        product.id,
        product.shopify_product_id,
        product.title,
        product.handle,
        product.status,
        product.vendor,
        product.product_type,
        product.created_at,
        product.updated_at,
        product.ingested_at
    )

    cur.execute(
            f"""UPDATE public.product
                SET id=%s, shopify_product_id=%s, title=%s, handle=%s, status=%s, vendor=%s, product_type=%s, created_at=%s, updated_at=%s, ingested_at=%s
                WHERE id=%s;""", 
            arguments
            )
    conn.commit()
    cur.close
    return {"mensaje": "product actualizado", "product": product}

def delete_product_repository(id: int):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
            f"""DELETE FROM public.product
                WHERE id = %s;""", 
            (id.id)
            )
    conn.commit()
    cur.close
    return {"mensaje": "product eliminado"}

def get_products_by_id_repository(id: int):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("select * from product where id = %s;",(id))
    rows = cur.fetchall()
    cur.close()
    return rows
