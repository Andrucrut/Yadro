from fastapi import FastAPI
from app.routers import user_router
from app.db import init_db
from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository
from app.db import AsyncSessionLocal

app = FastAPI(title="Random User API")

app.include_router(user_router.router)


@app.on_event("startup")
async def startup_event():
    await init_db()
    async with AsyncSessionLocal() as session:
        repo = UserRepository(session)
        service = UserService(repo)
        await service.fetch_users_from_api(1000)
