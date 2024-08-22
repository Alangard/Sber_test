from typing import AsyncGenerator
from datetime import datetime, timezone
from sqlalchemy import MetaData, create_engine, text
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

from app.config import settings

metadata = MetaData()

class BaseModel(DeclarativeBase):
    metadata = metadata

    created_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP(timezone=True), 
        server_default=text("TIMEZONE('utc', now())")
    )
    updated_at: Mapped[TIMESTAMP] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=text("TIMEZONE('utc', now())"),
        onupdate=datetime.now(timezone.utc)
    )


# DATABASE_URL_ASYNC = (f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASS}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}")

# engine = create_async_engine(DATABASE_URL_ASYNC)


# async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
#     async with async_session_maker() as session:
#         yield session