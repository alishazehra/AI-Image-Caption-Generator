from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from urllib.parse import quote_plus
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:password@localhost/todoapp")

engine = create_engine(DATABASE_URL, echo=True)

async_engine = create_async_engine(DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://"), echo=True)

def get_session() -> Session:
    with Session(engine) as session:
        yield session

AsyncSessionLocal = async_sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)

SQLModel.metadata.create_all(engine)