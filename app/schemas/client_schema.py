from pydantic import BaseModel

class ClientModel(BaseModel):
    p_name: str
    p_email: str
    p_phone_number: str
    p_address: str
    p_balance: int