from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ProductSchema(BaseModel):
    id: Optional[int] = Field(None, description="ID interno del producto (autoincremental)")
    shopify_product_id: int = Field(..., description="ID del producto en Shopify")
    title: str = Field(..., description="Título del producto")
    handle: Optional[str] = Field(None, description="Handle del producto (slug)")
    status: Optional[str] = Field(None, description="Estado del producto en Shopify")
    vendor: Optional[str] = Field(None, description="Vendedor o marca del producto")
    product_type: Optional[str] = Field(None, description="Tipo o categoría del producto")
    created_at: Optional[datetime] = Field(None, description="Fecha de creación en Shopify")
    updated_at: Optional[datetime] = Field(None, description="Fecha de última actualización en Shopify")
    ingested_at: Optional[datetime] = Field(default_factory=datetime.utcnow, description="Fecha de ingreso en el sistema")

    class Config:
        orm_mode = True
        from_attributes = True
        json_schema_extra = {
            "example": {
                "shopify_product_id": 1234567890,
                "title": "Camiseta edición limitada",
                "handle": "camiseta-edicion-limitada",
                "status": "active",
                "vendor": "MiMarca",
                "product_type": "Ropa",
                "created_at": "2025-10-16T15:30:00Z",
                "updated_at": "2025-10-16T15:45:00Z",
            }
        }
