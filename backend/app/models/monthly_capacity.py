from sqlalchemy import Column, Integer, Date, CheckConstraint
from app.db.base import Base

class MonthlyCapacity(Base):
    __tablename__ = "monthly_capacity"

    id = Column(Integer, primary_key=True, index=True)
    month = Column(Date, nullable=False, unique=True, index=True)
    total_slots = Column(Integer, nullable=False)
    booked_slots = Column(Integer, nullable=False)

    __table_args__ = (
        CheckConstraint("booked_slots >= 0", name="check_booked_non_negative"),
        CheckConstraint("booked_slots <= total_slots", name="check_booked_not_exceed_total"),
    )