import asyncio
import sys
import os
from logging.config import fileConfig
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, async_sessionmaker
from alembic import context
import nest_asyncio

nest_asyncio.apply()


# 📌 Add the absolute path of the backend directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# 📌 Import models (adjust the path according to your project structure)
from models import Base  

# 📌 Load Alembic configuration
config = context.config

# 📌 Configure logging using alembic.ini
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 📌 Retrieve the database URL from alembic.ini
DATABASE_URL = config.get_main_option("sqlalchemy.url")

# 📌 Create an asynchronous database engine
async_engine: AsyncEngine = create_async_engine(DATABASE_URL, future=True)

# 📌 Configure the async session factory
async_session = async_sessionmaker(async_engine, expire_on_commit=False)

# 📌 Define metadata target for autogenerate
target_metadata = Base.metadata  

# 📌 Function to run migrations in online mode
async def run_migrations_online():
    """Runs migrations in 'online' mode using an asynchronous connection."""
    async with async_engine.connect() as connection:
        await connection.run_sync(lambda conn: do_migrations(conn))

# 📌 Function to apply migrations
def do_migrations(connection):
    """Applies migrations using the provided database connection."""
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()

# 📌 Function to run migrations in offline mode
def run_migrations_offline():
    """Runs migrations in 'offline' mode, generating SQL scripts."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(url=url, target_metadata=target_metadata, literal_binds=True, dialect_opts={"paramstyle": "named"})
    
    with context.begin_transaction():
        context.run_migrations()

# 📌 Determine whether Alembic is running in offline or online mode
if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())  # Properly execute async migrations
