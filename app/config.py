import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 1️⃣ Read DB URL from environment (Render / local)
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL environment variable not set")

# 2️⃣ Create SQLAlchemy engine
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True   # avoids stale connection issues on Render
)

# 3️⃣ Session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# 4️⃣ Base class for models
Base = declarative_base()