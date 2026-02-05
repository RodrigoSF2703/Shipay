# conftest.py
import pytest
from httpx import AsyncClient
from main import app  # main.py está na raiz

@pytest.fixture
async def client():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
