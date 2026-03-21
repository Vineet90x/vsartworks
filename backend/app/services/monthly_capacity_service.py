from datetime import date
from sqlalchemy.orm import Session
from sqlalchemy import select, update
from app.models.monthly_capacity import MonthlyCapacity


def get_current_month_start():
    today = date.today()
    return date(today.year, today.month, 1)


def get_or_create_month(db: Session):
    month_start = get_current_month_start()

    record = db.query(MonthlyCapacity).filter(
        MonthlyCapacity.month == month_start
    ).first()

    if not record:
        record = MonthlyCapacity(month=month_start,total_slots=2,booked_slots=0)
        db.add(record)
        db.commit()
        db.refresh(record)

    return record


def get_available_slots(db: Session):
    record = get_or_create_month(db)
    return record.total_slots - record.booked_slots

def book_slot(db: Session):
    month_start = get_current_month_start()
    get_or_create_month(db)
    
    result = db.execute(
        update(MonthlyCapacity)
        .where(
            MonthlyCapacity.month == month_start,
            MonthlyCapacity.booked_slots < MonthlyCapacity.total_slots
        )
        .values(booked_slots=MonthlyCapacity.booked_slots + 1)
    )

    if result.rowcount == 0:
        return False

    db.commit()
    return True