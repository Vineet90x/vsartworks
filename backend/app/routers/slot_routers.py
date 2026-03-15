
from fastapi import Depends, APIRouter
from app.services.monthly_capacity_service import get_available_slots, book_slot
from sqlalchemy.orm import Session
from app.db.dependency import get_db

slot_router = APIRouter(prefix="/slots", tags=["Slots"])

@slot_router.get("/")
def available_slots(db: Session = Depends(get_db)):
    return {"available_slots": get_available_slots(db)}

@slot_router.post("/book")
def book_slot_endpoint(db: Session = Depends(get_db)):
    success = book_slot(db)
    if not success:
        return {"status": "failed", "message": "No slots available"}
    return {"status": "success", "message": "Slot booked"}
