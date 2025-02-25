from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# PostgreSQL connection URL (replace with your credentials)
DATABASE_URL = "postgresql+asyncpg://postgres:Pichincha+1864@localhost/image_generator"

# SQLAlchemy async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Session factory
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

async_session = SessionLocal

# Base model for ORM
Base = declarative_base()

# Dependency to get the database session
async def get_db():
    async with SessionLocal() as session:
        yield session
