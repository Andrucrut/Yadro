from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_session
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService
from app.schemas.user_schema import UserRead
from typing import List


async def get_user_service(session: AsyncSession = Depends(get_session)):
    repo = UserRepository(session)
    return UserService(repo)


async def fetch_users(count: int, service: UserService = Depends(get_user_service)):
    await service.fetch_users_from_api(count)
    return {"status": "ok", "count": count}


async def read_users(skip: int = 0, limit: int = 50, service: UserService = Depends(get_user_service)) -> List[UserRead]:
    return await service.get_users(skip, limit)


async def read_user(user_id: int, service: UserService = Depends(get_user_service)) -> UserRead:
    user = await service.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


async def random_user(service: UserService = Depends(get_user_service)) -> UserRead:
    user = await service.get_random_user()
    if not user:
        raise HTTPException(status_code=404, detail="No users found")
    return user
