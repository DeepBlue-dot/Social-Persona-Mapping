# backend/api/routes/osint_routes.py

from fastapi import APIRouter
from services.osint_service import collect_osint_data

router = APIRouter()

@router.post("/collect")
async def collect(username: str, platform: str):
    result = await collect_osint_data(username, platform)
    return result
