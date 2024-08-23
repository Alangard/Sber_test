import asyncio
import pytest
from typing import AsyncGenerator
from fastapi.testclient import TestClient
from httpx import ASGITransport, AsyncClient

from app.main import application
from app.config import settings

# from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
# from sqlalchemy.orm import sessionmaker

# from app.database import metadata 
# from app.database import get_async_session


#DATABASE
# DATABASE_URL_TEST_ASYNC = f"postgresql+asyncpg://{settings.DB_USER_TEST}:{settings.DB_PASS_TEST}@{settings.DB_HOST_TEST}:{settings.DB_PORT_TEST}/{settings.DB_NAME_TEST}"

# engine_test = create_async_engine(DATABASE_URL_TEST_ASYNC)
# async_session_maker = sessionmaker(engine_test, class_=AsyncSession, expire_on_commit=False)
# metadata.bind = engine_test

# async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
#     async with async_session_maker() as session:
#         yield session

# application.dependency_overrides[get_async_session] = override_get_async_session

# @pytest.fixture(autouse=True, scope='session')
# async def prepare_database():
#     async with engine_test.begin() as conn:
#         await conn.run_sync(metadata.create_all)
#     yield
#     async with engine_test.begin() as conn:
# #         await conn.run_sync(metadata.drop_all)

# SETUP

client = TestClient(application)

@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(transport=ASGITransport(app=application), base_url=f"{settings.DOMAIN_NAME}{settings.api_prefix}") as ac:
        yield ac