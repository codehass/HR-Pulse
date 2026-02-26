import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api.routers import auth, jobs
from .config import settings
from .db.database import Base, engine

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)

    yield
    print("Shutting down...")


app = FastAPI(
    title="HR puls",
    lifespan=lifespan,
    description=(
        "This API provides endpoints for users to authenticate and ask HR puls!"
    ),
)

origins = [settings.FRONTEND_URL]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(jobs.router)


@app.get("/", tags=["Home route"])
def get_home():
    return {"message": "Hello to HR PULS API"}
