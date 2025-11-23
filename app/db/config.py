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

# Read environment variables
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")   # MUST be unix socket path
DB_NAME = os.getenv("DB_NAME")

# --- 🔥 Use UNIX socket inside Cloud Run ---
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASS}@/{DB_NAME}?unix_socket={DB_HOST}"

engine = create_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()