from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#sqlalchemy is a python library that provides an object relational mapper(orm).It basically maps databases to python objects.
SQLALCHEMY_DATABASE_URL = "sqlite:///address.db"

#connect with the database
engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind= engine , autocommit=False, autoflush=False)
#Session manages persistence operations for ORM-mapped objects
#Sessionmaker is a configurabel session factory


#The declarative_base() function is used to create base class. 
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close

