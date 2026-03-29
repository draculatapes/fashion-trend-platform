"""Trend routes — list and create fashion trends."""

from datetime import datetime, timezone

from bson import ObjectId
from fastapi import APIRouter, Depends, Query
from typing import Optional, List

from auth import get_current_user
from database import get_database
from models import TrendCreate, TrendResponse

router = APIRouter(prefix="/api/trends", tags=["Trends"])


@router.get("/", response_model=List[TrendResponse])
async def list_trends(region: Optional[str] = Query(None, description="Filter by region slug")):
    """Public — list all trends, with optional region filter."""
    db = get_database()

    query = {}
    if region:
        query["region_slug"] = region

    trends = []
    cursor = db.trends.find(query).sort("created_at", -1)
    async for trend in cursor:
        # Optionally embed region data
        region_doc = None
        if trend.get("region_slug"):
            region_doc = await db.regions.find_one({"slug": trend["region_slug"]})
            if region_doc:
                region_doc = {
                    "id": str(region_doc["_id"]),
                    "name": region_doc["name"],
                    "slug": region_doc["slug"],
                }

        trends.append(
            TrendResponse(
                id=str(trend["_id"]),
                title=trend["title"],
                region=region_doc,
                category=trend["category"],
                status=trend["status"],
                created_at=trend["created_at"],
            )
        )
    return trends


@router.post("/", response_model=TrendResponse, status_code=201)
async def create_trend(trend_data: TrendCreate, current_user: dict = Depends(get_current_user)):
    """Protected — create a new trend (JWT required)."""
    db = get_database()

    trend_doc = {
        "title": trend_data.title,
        "region_slug": trend_data.region_slug,
        "category": trend_data.category.value,
        "status": trend_data.status.value,
        "created_by": str(current_user["_id"]),
        "created_at": datetime.now(timezone.utc),
    }
    result = await db.trends.insert_one(trend_doc)

    # Embed region data in response
    region_doc = await db.regions.find_one({"slug": trend_data.region_slug})
    region_info = None
    if region_doc:
        region_info = {
            "id": str(region_doc["_id"]),
            "name": region_doc["name"],
            "slug": region_doc["slug"],
        }

    return TrendResponse(
        id=str(result.inserted_id),
        title=trend_data.title,
        region=region_info,
        category=trend_data.category.value,
        status=trend_data.status.value,
        created_at=trend_doc["created_at"],
    )
