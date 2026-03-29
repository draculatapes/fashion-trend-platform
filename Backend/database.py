"""Async MongoDB connection using motor."""

import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "fashion_trends")

client: AsyncIOMotorClient = None
db = None


async def connect_to_mongo():
    """Create MongoDB connection on startup."""
    global client, db
    client = AsyncIOMotorClient(MONGODB_URL)
    db = client[DB_NAME]
    print(f"✅ Connected to MongoDB: {DB_NAME}")


async def close_mongo_connection():
    """Close MongoDB connection on shutdown."""
    global client
    if client:
        client.close()
        print("❌ Disconnected from MongoDB")


def get_database():
    """Return the database instance."""
    return db
