from pydantic import BaseModel
from .db import Base

#Pydantic is primarily a parsing library. It guarantees the types and constraints of the output model.

class Address(BaseModel):
    street: str
    city: str
    state: str
    zip: str
    lat: float
    lng: float

    class Config():
        orm_mode = True


class ShowAddress(BaseModel):
    lat: float
    lng: float

    class Config():
        orm_mode = True