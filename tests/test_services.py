# tests/test_services.py
import pytest
from unittest.mock import AsyncMock, patch
from app.services.user_service import UserService
from app.models import User
import uuid



@pytest.mark.asyncio
async def test_get_users(session):
    repo = AsyncMock()
    repo.get_all.return_value = [
        User(
            id=1,
            uuid=uuid.uuid4(),
            gender="male",
            first_name="John",
            last_name="Doe",
            phone="1234567890",
            email="john@example.com",
            city="New York",
            country="USA",
            picture="http://example.com/pic.jpg"
        )
    ]

    service = UserService(repo)
    users = await service.get_users()
    assert len(users) == 1
    assert users[0].first_name == "John"


@pytest.mark.asyncio
async def test_get_random_user(session):
    repo = AsyncMock()
    repo.get_random_user.return_value = User(
        id=1,
        uuid=uuid.uuid4(),
        gender="female",
        first_name="Jane",
        last_name="Doe",
        phone="0987654321",
        email="jane@example.com",
        city="Los Angeles",
        country="USA",
        picture="http://example.com/jane.jpg"
    )

    service = UserService(repo)
    user = await service.get_random_user()
    assert user is not None
    assert user.first_name == "Jane"