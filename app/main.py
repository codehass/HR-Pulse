import os

from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

from .db.database import Base, engine

load_dotenv()
FRONTEND_URL = os.getenv("FRONTEND_URL")

app = FastAPI()

origins = [FRONTEND_URL]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)


@app.get("/")
def get_home():
    return {"message": "Hello to our sentiment api!!"}
