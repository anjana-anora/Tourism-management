from fastapi import APIRouter
from models.Passengers import Passengers
from db_config import PASSENGERS
from bson import ObjectId
passengers = APIRouter()

def display_object(item):
    item['_id'] = str(item['_id'])
    return item

@passengers.get('/')
def show_all_passengers():
    res=[]
    for document in PASSENGERS.find():
        res.append(display_object(document))
    print('No of passengers registered: ', len(res))
    return res

@passengers.get('/{id}')
def show_passenger_by_id(id:str):
    return PASSENGERS.find_one({'_id':id})

@passengers.post('/add')
def add_a_passenger(passenger: Passengers):
    PASSENGERS.insert_one(passenger.model_dump())
    return True

@passengers.put('/rate')
def rate_package(id:str, value:float):
    pass

@passengers.get('/packagezz')
def passengers_enrolled():
    res=[]
    for document in PASSENGERS.find():
        res.append(display_object(document))
    print('result:', res)
    return res