from fastapi import FastAPI
from .config import get_settings
from .views import client_view

settings = get_settings()
app = FastAPI(title=settings.app_name)

# Mount routers (Views in MVC)
app.include_router(client_view.router, prefix="/clients", tags=["clients"])

@app.get("/health", tags=["health"])
def health():
    mensaje = 'Esto funciona'
    return {"status": mensaje}
