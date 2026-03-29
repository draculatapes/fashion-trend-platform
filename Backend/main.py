"""FastAPI application — CORS, lifespan events, route includes."""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import connect_to_mongo, close_mongo_connection
from routes.auth_routes import router as auth_router
from routes.trend_routes import router as trend_router
from routes.region_routes import router as region_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup / shutdown lifecycle."""
    await connect_to_mongo()
    yield
    await close_mongo_connection()


app = FastAPI(
    title="Fashion Trend Platform API",
    description="API for tracking and exploring fashion trends across regions.",
    version="1.0.0",
    lifespan=lifespan,
)

# ── CORS ───────────────────────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # tighten in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Routes ─────────────────────────────────────────────────────────────
app.include_router(auth_router)
app.include_router(trend_router)
app.include_router(region_router)


@app.get("/", tags=["Health"])
async def root():
    return {"message": "Fashion Trend Platform API is running 🚀"}
