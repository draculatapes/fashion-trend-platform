"""Pydantic schemas for request/response validation."""

from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, EmailStr, Field


# ── Enums ──────────────────────────────────────────────────────────────

class TrendCategory(str, Enum):
    streetwear = "streetwear"
    haute_couture = "haute_couture"
    casual = "casual"
    sportswear = "sportswear"
    sustainable = "sustainable"
    accessories = "accessories"
    footwear = "footwear"


class TrendStatus(str, Enum):
    emerging = "emerging"
    trending = "trending"
    declining = "declining"
    stable = "stable"


# ── User Schemas ───────────────────────────────────────────────────────

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6)


class UserResponse(BaseModel):
    id: str
    username: str
    email: str
    created_at: datetime


# ── Token Schema ───────────────────────────────────────────────────────

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


# ── Trend Schemas ──────────────────────────────────────────────────────

class TrendCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    region_slug: str
    category: TrendCategory
    status: TrendStatus = TrendStatus.emerging


class TrendResponse(BaseModel):
    id: str
    title: str
    region: Optional[dict] = None
    category: str
    status: str
    created_at: datetime


# ── Region Schemas ─────────────────────────────────────────────────────

class RegionCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    slug: str = Field(..., min_length=1, max_length=50)


class RegionResponse(BaseModel):
    id: str
    name: str
    slug: str
    created_at: datetime
