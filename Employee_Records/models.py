from sqlalchemy import Column, Integer, String
from database import Base
class DBRecords(Base):
    __tablename__ = "Records"
    Employee_id = Column(Integer, primary_key=True)
    Employee_Name = Column(String(50))
