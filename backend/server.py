from fastapi import FastAPI
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL = "postgresql+asyncpg://postgres:Pichincha+1864@localhost/image_generator"

app = FastAPI()

# Set up the database engine
engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

@app.get("/")
async def read_root():
    return {"message": "Connected to PostgreSQL!"}
