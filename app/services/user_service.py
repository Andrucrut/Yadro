import httpx
from app.models import User
from uuid import UUID
from app.repositories.user_repository import UserRepository


class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    async def fetch_users_from_api(self, count: int):
        async with httpx.AsyncClient() as client:
            resp = await client.get(f'https://randomuser.me/api/?results={count}')
            data = resp.json()["results"]

        users = [
            User(
                uuid=UUID(u["login"]["uuid"]),
                gender=u["gender"],
                first_name=u["name"]["first"],
                last_name=u["name"]["last"],
                phone=u["phone"],
                email=u["email"],
                city=u["location"]["city"],
                country=u["location"]["country"],
                picture=u["picture"]["thumbnail"]
            )
            for u in data
        ]
        await self.repo.add_users(users)

    async def get_users(self, skip: int = 0, limit: int = 50):
        return await self.repo.get_all(skip, limit)

    async def get_user_by_id(self, user_id: int):
        return await self.repo.get_by_id(user_id)

    async def get_random_user(self):
        return await self.repo.get_random_user()
