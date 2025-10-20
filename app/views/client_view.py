from fastapi import APIRouter, HTTPException
from ..controllers.cient_controller import get_clients_controller, create_client_repository
from app.schemas.client_schema import ClientModel

router = APIRouter(prefix="/clients", tags=["clients"])


@router.get("/")
def get_clients_view():
    try:
        return get_clients_controller()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/")
def create_client_view(client: ClientModel):
    try:
        return create_client_repository(client)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
