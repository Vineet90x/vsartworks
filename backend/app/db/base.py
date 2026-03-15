from sqlalchemy.orm import declarative_base

Base = declarative_base()

# Import all models here
from app.models.monthly_capacity import MonthlyCapacity