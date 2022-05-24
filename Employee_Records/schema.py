from pydantic import BaseModel

#Create Record model
class RecordCreate(BaseModel):
    Employee_Name : str

class Record(BaseModel):
    Employee_id: int
    Employee_Name: str

    class Config:
        orm_mode = True
