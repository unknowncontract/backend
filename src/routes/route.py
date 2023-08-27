from fastapi import APIRouter
from .image import router as image_router

routers = [image_router]

router = APIRouter(
    prefix=""
)

for r in routers:
    router.include_router(r)
