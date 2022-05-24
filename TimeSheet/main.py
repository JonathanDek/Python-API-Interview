from email.policy import HTTP
from http.client import HTTPException
from fastapi import Depends, FastAPI, status
from requests import session
from sqlalchemy.orm import Session
from database import Base, SessionLocal, engine
from typing import List
import models
import schema
from datetime import date

app = FastAPI()

#Create Database
Base.metadata.create_all(bind=engine)

#Get DB
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

@app.get("/")
def root():
    return "TimeSheet app"

@app.post("/TimeSheet", status_code=status.HTTP_201_CREATED)
def create_TimeSheet(timesheet: schema.TimeSheetCreate, session: Session = Depends(get_session)):

    timesheet_db  = models.TimeSheetDB(Employee_Id= timesheet.Employee_Id, Employee_Name = timesheet.Employee_Name, Date = timesheet.Date, hours = timesheet.hours)

    session.add(timesheet_db)
    session.commit()
    session.refresh(timesheet_db)

    session.close
    return session

@app.get("/TimeSheets/{id}", response_model=List[schema.TimeSheet])
def get_TimeSheet(e_id:int):

    session = Session(bind=engine, expire_on_commit=False)

    sheet_list = session.query(models.TimeSheetDB)\
        .filter(models.TimeSheetDB.Employee_Id == e_id)\
        .all()
    
    session.close
    return sheet_list

@app.get("/TimeSheet/{id}", response_model=List[schema.TimeSheet])
def get_TimeSheetDate(e_id:int, year:int, month:int, day:int):

    session = Session(bind=engine, expire_on_commit=False)

    sheet_list = session.query(models.TimeSheetDB)\
        .filter(models.TimeSheetDB.Employee_Id==e_id, models.TimeSheetDB.Date == date(year,month,day))\
        .all()
    session.close
    return sheet_list