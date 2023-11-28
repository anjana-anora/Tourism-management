from fastapi import APIRouter, HTTPException, status
from db_config import PACKAGES
from models.Packages import Packages
from bson import ObjectId

packages = APIRouter()

def display_object(item):
    item['_id'] = str(item['_id'])

    return item

@packages.get('/')
def show_all_packages():
    res = []
    for document in PACKAGES.find():     
        res.append(display_object(document))        
    res.append({'available packages':len(res)})
    return res

@packages.get('/{id}')
def get_package_by_id(id:str):
    res = PACKAGES.find_one({'_id':ObjectId(id)})
    if not res:
        raise HTTPException(status_code=404, detail='No corresponding data')
    res['_id'] = str(res['_id'])
    return res

@packages.post('/add')
def add_a_package(package : Packages):
    print(PACKAGES.insert_one(package.model_dump()))
    return {package.name : 'package created'}

@packages.delete('/remove')
def remove_package(id: str):
    PACKAGES.delete_one({'_id':ObjectId(id)})
    if not PACKAGES.find_one({'_id':ObjectId(id)}):
        raise HTTPException(status_code=404, detail='No data')
    return {'success': 'deleted'}