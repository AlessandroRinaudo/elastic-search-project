from fastapi import FastAPI
from app.routers import search, upload

app = FastAPI()

app.include_router(search.router)
app.include_router(upload.router)
