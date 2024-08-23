import pytest
from typing import AsyncGenerator
from fastapi.testclient import TestClient
from httpx import ASGITransport, AsyncClient

from app.main import application
from app.config import settings


# SETUP
client = TestClient(application)


@pytest.fixture(scope="session")
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(
        transport=ASGITransport(app=application),
        base_url=f"{settings.DOMAIN_NAME}{settings.api_prefix}",
    ) as ac:
        yield ac
