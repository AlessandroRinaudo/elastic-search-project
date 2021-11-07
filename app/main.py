from fastapi import FastAPI
from app.routers import search, upload
import os

print(os.environ["test"])
app = FastAPI()

app.include_router(search.router)
app.include_router(upload.router)
