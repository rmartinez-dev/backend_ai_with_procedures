from app.repositories.client_repository import get_clients_repository, create_client_repository
from app.schemas.client_schema import ClientModel

def get_clients_controller():
    clients = get_clients_repository()
    return clients


def create_client_controller(client: ClientModel):
    create_client_repository(client)
