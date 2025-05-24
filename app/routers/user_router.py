from fastapi import APIRouter
from app.controllers import user_controller

router = APIRouter()


router.post("/load")(user_controller.fetch_users)
router.get("/")(user_controller.read_users)
router.get("/user/{user_id}")(user_controller.read_user)
router.get("/random")(user_controller.random_user)
