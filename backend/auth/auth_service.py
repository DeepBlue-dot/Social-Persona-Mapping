from passlib.context import CryptContext
from auth.jwt_handler import create_jwt

# Use argon2 instead of bcrypt
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

# Mock database (replace with real DB later)
fake_users_db = {
    "admin": {
        "username": "admin",
        "password": pwd_context.hash("admin123"),   # hashed with argon2
        "role": "admin"
    }
}

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(username: str, password: str):
    user = fake_users_db.get(username)
    if not user:
        return None

    if not verify_password(password, user["password"]):
        return None

    return user

def login_user(username: str, password: str):
    user = authenticate_user(username, password)
    if not user:
        return None

    token = create_jwt({"sub": user["username"], "role": user["role"]})
    return {"access_token": token, "token_type": "bearer"}
