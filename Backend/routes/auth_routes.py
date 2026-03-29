"""Auth routes — signup and login endpoints."""

from datetime import datetime, timezone

from bson import ObjectId
from fastapi import APIRouter, HTTPException, status

from auth import create_access_token, hash_password, verify_password
from database import get_database
from models import TokenResponse, UserCreate, UserResponse

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/signup", response_model=TokenResponse, status_code=status.HTTP_201_CREATED)
async def signup(user_data: UserCreate):
    """Register a new user and return a JWT token."""
    db = get_database()

    # Check if username or email already exists
    existing = await db.users.find_one(
        {"$or": [{"username": user_data.username}, {"email": user_data.email}]}
    )
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Username or email already registered",
        )

    # Create user document
    user_doc = {
        "username": user_data.username,
        "email": user_data.email,
        "password": hash_password(user_data.password),
        "created_at": datetime.now(timezone.utc),
    }
    result = await db.users.insert_one(user_doc)

    # Generate JWT
    token = create_access_token(str(result.inserted_id))
    return TokenResponse(access_token=token)


@router.post("/login", response_model=TokenResponse)
async def login(user_data: UserCreate):
    """Authenticate user and return a JWT token."""
    db = get_database()

    user = await db.users.find_one({"email": user_data.email})
    if not user or not verify_password(user_data.password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    token = create_access_token(str(user["_id"]))
    return TokenResponse(access_token=token)
