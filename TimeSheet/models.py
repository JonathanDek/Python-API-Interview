from sqlalchemy import String, Integer, Column, Date
from database import Base
class TimeSheetDB(Base):
    __tablename__ = "TimeSheets"
    TimeSheet_Id = Column(Integer, primary_key=True)
    Employee_Id = Column(Integer)
    Employee_Name = Column(String(50))
    Date = Column(Date)
    hours = Column(Integer)