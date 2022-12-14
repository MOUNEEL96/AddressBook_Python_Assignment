from .db import Base
from sqlalchemy import Column, Integer, String, Float

#Model for table creation
class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True, index=True)
    street = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    zip = Column(String, nullable=False)
    lat = Column(Float, nullable=False)
    lng = Column(Float, nullable=False)


    
