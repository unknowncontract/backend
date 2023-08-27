from fastapi import APIRouter

router = APIRouter(
    prefix="/image",
    tags=['image']
)

@router.get("/{id}")
async def findById(id: str):
    return id