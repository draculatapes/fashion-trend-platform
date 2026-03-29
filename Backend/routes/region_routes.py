"""Region routes — list and create regions."""

from datetime import datetime, timezone
from typing import List

from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException, status

from auth import get_current_user
from database import get_database
from models import RegionCreate, RegionResponse

router = APIRouter(prefix="/api/regions", tags=["Regions"])


@router.get("/", response_model=List[RegionResponse])
async def list_regions():
    """Public — list all regions."""
    db = get_database()

    regions = []
    cursor = db.regions.find().sort("name", 1)
    async for region in cursor:
        regions.append(
            RegionResponse(
                id=str(region["_id"]),
                name=region["name"],
                slug=region["slug"],
                created_at=region["created_at"],
            )
        )
    return regions


@router.post("/", response_model=RegionResponse, status_code=201)
async def create_region(region_data: RegionCreate, current_user: dict = Depends(get_current_user)):
    """Protected — create a new region (JWT required)."""
    db = get_database()

    # Check if slug already exists
    existing = await db.regions.find_one({"slug": region_data.slug})
    if existing:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Region with slug '{region_data.slug}' already exists",
        )

    region_doc = {
        "name": region_data.name,
        "slug": region_data.slug,
        "created_by": str(current_user["_id"]),
        "created_at": datetime.now(timezone.utc),
    }
    result = await db.regions.insert_one(region_doc)

    return RegionResponse(
        id=str(result.inserted_id),
        name=region_data.name,
        slug=region_data.slug,
        created_at=region_doc["created_at"],
    )
