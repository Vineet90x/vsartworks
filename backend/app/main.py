from fastapi import FastAPI
from fastapi.security import HTTPBearer
from app.db.base import Base
from app.db.session import engine
from app.routers.slot_routers import slot_router

security = HTTPBearer()

app = FastAPI(title="VSART API",swagger_ui_parameters={"persistAuthorization": True})

Base.metadata.create_all(bind=engine)
    
@app.get("/")
def root():
    return {"message": "VSART API Running"}

app.include_router(slot_router)
