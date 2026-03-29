"""Seed script — populate MongoDB with sample regions and trends."""

import asyncio
from datetime import datetime, timezone

from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "fashion_trends")

SAMPLE_REGIONS = [
    {"name": "India", "slug": "india"},
    {"name": "United States", "slug": "usa"},
    {"name": "Europe", "slug": "europe"},
    {"name": "Japan", "slug": "japan"},
    {"name": "South Korea", "slug": "south-korea"},
    {"name": "United Kingdom", "slug": "uk"},
    {"name": "Brazil", "slug": "brazil"},
    {"name": "Middle East", "slug": "middle-east"},
]

SAMPLE_TRENDS = [
    {"title": "Oversized Blazers", "region_slug": "india", "category": "casual", "status": "trending"},
    {"title": "Neon Streetwear", "region_slug": "japan", "category": "streetwear", "status": "emerging"},
    {"title": "Sustainable Denim", "region_slug": "europe", "category": "sustainable", "status": "trending"},
    {"title": "Chunky Sneakers", "region_slug": "usa", "category": "footwear", "status": "stable"},
    {"title": "Minimalist Handbags", "region_slug": "south-korea", "category": "accessories", "status": "emerging"},
    {"title": "Athleisure Sets", "region_slug": "usa", "category": "sportswear", "status": "trending"},
    {"title": "Embroidered Kurtas", "region_slug": "india", "category": "haute_couture", "status": "stable"},
    {"title": "Vintage Y2K Revival", "region_slug": "uk", "category": "streetwear", "status": "trending"},
    {"title": "Eco-Friendly Activewear", "region_slug": "brazil", "category": "sustainable", "status": "emerging"},
    {"title": "Modest Fashion", "region_slug": "middle-east", "category": "casual", "status": "trending"},
    {"title": "Techwear Jackets", "region_slug": "japan", "category": "streetwear", "status": "trending"},
    {"title": "Pastel Power Suits", "region_slug": "europe", "category": "haute_couture", "status": "emerging"},
]


async def seed():
    client = AsyncIOMotorClient(MONGODB_URL)
    db = client[DB_NAME]

    # Clear existing data
    await db.regions.delete_many({})
    await db.trends.delete_many({})

    now = datetime.now(timezone.utc)

    # Seed regions
    for region in SAMPLE_REGIONS:
        region["created_at"] = now
    await db.regions.insert_many(SAMPLE_REGIONS)
    print(f"✅ Seeded {len(SAMPLE_REGIONS)} regions")

    # Seed trends
    for trend in SAMPLE_TRENDS:
        trend["created_at"] = now
    await db.trends.insert_many(SAMPLE_TRENDS)
    print(f"✅ Seeded {len(SAMPLE_TRENDS)} trends")

    client.close()
    print("🎉 Seed complete!")


if __name__ == "__main__":
    asyncio.run(seed())
