from dotenv import load_dotenv
from fastapi.responses import PlainTextResponse

load_dotenv()

from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine, get_db
from .utils.rate_limit import limiter
from app.routers import email, price, report, report_image, press_release, auth, category, news_room_category


from slowapi.errors import RateLimitExceeded
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address

from fastapi.staticfiles import StaticFiles

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/images", StaticFiles(directory="images"), name="images")

origins = [
    "https://localhost:3000",
    "http://localhost:3000",
    "http://visionaryadmin.onrender.com",
    "https://visionaryadmin.onrender.com",
    "https://resilient-douhua-706e26.netlify.app",
    "http://resilient-douhua-706e26.netlify.app",
    "https://visionary-market-research.onrender.com",
    "http://visionary-market-research.onrender.com",
    "https://178765.xyz",
    "http://178765.xyz",
    "https://visionarynextjs-nextjs.7c2g7o.easypanel.host",
    "http://visionarynextjs-nextjs.7c2g7o.easypanel.host",
    "https://visionarynextjs-admin-console.7c2g7o.easypanel.host",
    "http://visionarynextjs-admin-console.7c2g7o.easypanel.host",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"greeting": "Hello!", "message": "This api works!"}


app.include_router(news_room_category.router, prefix="/news_room_category", tags=["News Room Category"])
app.include_router(category.router, prefix="/category", tags=["Category"])
app.include_router(report.router, prefix="/reports", tags=["Report"])
app.include_router(report_image.router, prefix="/report_images", tags=["Report Image"]) 
app.include_router(press_release.router, prefix="/press_release", tags=["Press Release"]) 
app.include_router(price.router, prefix="/price", tags=["Price"])
app.include_router(auth.router, tags=["Auth"])
app.include_router(email.router, tags=["Email"])

