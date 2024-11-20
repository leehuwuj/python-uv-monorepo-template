from core.hello import greet  # Import from core package
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def health():
    return {"status": "ok", "message": greet()}
