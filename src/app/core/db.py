from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy import MetaData

from src.app.core.config import get_config

_settings = get_config()
engine = create_async_engine(_settings.db_url,  pool_pre_ping=True, echo="debug", future=True) 

# echo=False → No SQL logs (default).
# echo=True → Logs SQL and parameter values at the INFO level.
# echo="debug" → More verbose, logs extra info (like connection pool checkouts) at the DEBUG level.

SessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)
Base = declarative_base(metadata=MetaData(schema="linkedin"))

async def get_db() -> AsyncSession:
    db = SessionLocal()
    try:
        yield db
        await db.commit()    # commit everything at the end of the request
    except:
        await db.rollback()  # roll back on error
        raise
    finally:
        await db.close()
