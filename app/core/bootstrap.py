# Optional helper to create tables during dev
from sqlalchemy import create_engine
from ..config import get_settings
from ..models.user import Base

def init_db():
    engine = create_engine(get_settings().database_url, connect_args={"check_same_thread": False} if get_settings().database_url.startswith("sqlite") else {})
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    init_db()
    print("Database initialized.")
