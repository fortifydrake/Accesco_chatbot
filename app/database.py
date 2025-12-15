from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from app.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    poolclass=NullPool,              # 🔴 REQUIRED FOR SUPABASE POOLER
    connect_args={"sslmode": "require"},
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()