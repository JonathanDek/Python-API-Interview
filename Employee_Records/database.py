from tokenize import String
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

#SqlAlchemy Setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./Records.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
