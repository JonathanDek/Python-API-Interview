from email.policy import HTTP
from http.client import HTTPException
from fastapi import Depends, FastAPI, status
from sqlalchemy.orm import Session
from database import Base, SessionLocal, engine
from typing import List
import models
import schema

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
    return "Records app"

@app.post("/Record", status_code=status.HTTP_201_CREATED)
def create_record(record : schema.RecordCreate, session: Session = Depends(get_session)):

    #create instance of record db
    record_db = models.DBRecords(Employee_Name = record.Employee_Name)

    #Add to session and commit
    session.add(record_db)
    session.commit()
    session.refresh(record_db)

    #close session
    session.close()
    return record_db

@app.get("/Record/{id}",response_model=schema.Record)
def get_record(id:int):
    #Create a new session
    session = Session(bind=engine, expire_on_commit=False)

    #Grab requested ID
    record = session.query(models.DBRecords).get(id)

    #Close Session
    session.close()
    if not record:
        raise HTTPException(status_code=400, detail=f"Employee with ID: {id} not found")
    return record

@app.get("/Records", response_model= List[schema.Record])
def get_records():
    #Create a new session
    session = Session(bind=engine, expire_on_commit=False)

    #Grab requested ID
    record_List = session.query(models.DBRecords).all()

    #Close Session
    session.close()
    return record_List
