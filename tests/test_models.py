# tests/test_models.py
from app.models import User
import uuid


def test_user_model():
    user_uuid = uuid.uuid4()
    user = User(
        uuid=user_uuid,
        gender="male",
        first_name="John",
        last_name="Doe",
        phone="1234567890",
        email="john@example.com",
        city="New York",
        country="USA",
        picture="http://example.com/pic.jpg"
    )

    assert user.uuid == user_uuid
    assert user.gender == "male"
    assert user.first_name == "John"
    assert user.last_name == "Doe"
    assert user.phone == "1234567890"
    assert user.email == "john@example.com"
    assert user.city == "New York"
    assert user.country == "USA"
    assert user.picture == "http://example.com/pic.jpg"
    assert user.id is None