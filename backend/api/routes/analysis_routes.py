# backend/api/routes/analysis_routes.py

from fastapi import APIRouter
from services.analysis_service import analyze_accounts

router = APIRouter()

@router.post("/account-linking")
async def account_linking(target_username: str):
    score = await analyze_accounts(target_username)
    return score
