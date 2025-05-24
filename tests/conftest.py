import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession
from app.main import app
from app.db import get_session, async_engine
from sqlmodel import SQLModel
from app.db import AsyncSessionLocal


@pytest.fixture(scope="session")
async def prepare_database():
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)
        await conn.run_sync(SQLModel.metadata.create_all)


@pytest.fixture
async def session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session


@pytest.fixture
async def client(prepare_database):
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac
