from fastapi import FastAPI, Depends
from sqlalchemy import text
from app.db.base import Base
from app.db.session import engine
from app.services.monthly_capacity_service import get_available_slots
from sqlalchemy.orm import Session
from app.db.dependency import get_db
from app.routers.slot_routers import slot_router

app = FastAPI(title="VSART API")

Base.metadata.create_all(bind=engine)
    
@app.get("/")
def root():
    return {"message": "VSART API Running"}

app.include_router(slot_router)