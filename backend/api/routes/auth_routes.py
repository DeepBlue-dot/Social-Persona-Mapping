from fastapi import APIRouter, HTTPException
from auth.auth_service import login_user

router = APIRouter()

@router.post("/login")
def login(username: str, password: str):
    auth = login_user(username, password)
    if not auth:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return auth
