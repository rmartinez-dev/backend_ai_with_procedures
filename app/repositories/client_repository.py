from app.core.db import get_db_connection
from app.schemas.client_schema import ClientModel
import psycopg2.extras


def get_clients_repository():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute("select * from clients;")
    rows = cur.fetchall()
    cur.close()
    return rows


def create_client_repository(client: ClientModel):
    conn = get_db_connection()
    cur = conn.cursor()

    arguments = (
        client.p_name, 
        client.p_email, 
        client.p_phone_number, 
        client.p_address, 
        client.p_balance
    )
    cur.execute(f"""
                INSERT INTO clients (name, email, phone_number, address, balance) 
                VALUES (%s, %s, %s, %s, %s);""", arguments)
    conn.commit()
    cur.close
    return {"mensaje": "cliente creado", "cliente": client}
