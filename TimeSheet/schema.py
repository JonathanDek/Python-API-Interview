from pydantic import BaseModel
from datetime import date
#Create Timesheet Model
class TimeSheetCreate(BaseModel):
    Employee_Id:int
    Employee_Name:str
    Date:date
    hours:int

class TimeSheet(BaseModel):
    TimeSheet_Id:int
    Employee_Id:int
    Employee_Name:str
    Date:date
    hours:int

    class Config:
        orm_mode=True