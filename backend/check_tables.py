import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text
from database import SessionLocal 

async def check_tables():
    async with SessionLocal() as session:
        result = await session.execute(text("SELECT tablename FROM pg_tables WHERE schemaname = 'public'"))
        tables = result.scalars().all()
        print("Existing tables:", tables)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(check_tables())
