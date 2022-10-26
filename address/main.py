from typing import Optional
from fastapi import FastAPI , Depends , Response
from .import schemas , db , models
from .db import engine
from sqlalchemy.orm import Session 

app = FastAPI()


get_db = db.get_db

#Create and store data in the tables
models.Base.metadata.create_all(engine)

# CRUD operations---->
@app.get("/")
def index():
    return {"Check": "Docs Page"}


@app.get("/addresses/")
def get_all(db : Session = Depends(get_db)):
    address = db.query(models.Address).all()
    return address


@app.post('/createaddress/',response_model=schemas.Address) 
def create_address(request: schemas.Address,db : Session = Depends(get_db)):
    new_address = models.Address(**request.dict())
    print(new_address)
    db.add(new_address)
    db.commit()
    return new_address


@app.get('/addresses/{id}')
def get_address(id: int,db : Session = Depends(get_db)):
    address = db.query(models.Address).filter(models.Address.id == id).first()
    return address


@app.delete('/addresses/{id}')
def delete_address(id: int,db : Session = Depends(get_db)):
    address = db.query(models.Address).filter(models.Address.id == id).first()
    db.delete(address)
    db.commit()
    return {"message": "Address deleted"}


@app.put('/addresses/{id}', response_model=schemas.Address)
def update_address(id: int, request: schemas.Address,db : Session = Depends(get_db)):
   new_address = db.query(models.Address).filter(models.Address.id == id).all()
   new_address.street = request.street
   new_address.city = request.city
   new_address.state = request.state
   new_address.zip = request.zip
   new_address.lat = request.lat
   new_address.lng = request.lng
   db.commit()
   db.refresh(new_address)
   return new_address


# retrieve all the addresses that are between the coordinates 
@app.get('/addresses/{lat}/{lng}')
def get_address_by_coordinates(lat: float, lng: float,db : Session = Depends(get_db)):
    retrieve_address = db.query(models.Address).filter(models.Address.lat <= lat, models.Address.lng <= lng).all()
    return retrieve_address



