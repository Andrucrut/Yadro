from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from app.models import User
from typing import List, Optional
from uuid import UUID
import random


class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def add_users(self, users: List[User]):
        self.session.add_all(users)
        await self.session.commit()

    async def get_all(self, skip: int = 0, limit: int = 50) -> List[User]:
        result = await self.session.execute(select(User).offset(skip).limit(limit))
        return result.scalars().all()

    async def get_by_id(self, user_id: int) -> Optional[User]:
        result = await self.session.execute(select(User).where(User.id == user_id))
        return result.scalar_one_or_none()

    async def get_random_user(self) -> Optional[User]:
        result = await self.session.execute(select(User))
        users = result.scalars().all()
        return random.choice(users) if users else None
