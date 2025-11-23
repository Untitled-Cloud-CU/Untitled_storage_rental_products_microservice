"""
Database configuration and SQLAlchemy session setup
Loads values from .env using python-dotenv.
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load .env variables into Python process
load_dotenv()

# Read environment variables (must exist in .env OR in Cloud Run env)
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_PORT = os.getenv("DB_PORT", "3306")  # default 3306 if not provided

# Build SQLAlchemy connection string
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create engine (main.py imports this)
engine = create_engine(
    DATABASE_URL,
    echo=True,         # log SQL queries - keep ON for dev
    pool_pre_ping=True
)

# Session factory (used via FastAPI dependency)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """
    Get a database session.
    Always close after use.
    FastAPI will call this per-request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()