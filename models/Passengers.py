from pydantic import BaseModel
from datetime import datetime
from bson import objectid

class Passengers(BaseModel):
    name: str
    travel_date: datetime
    rating: float = 0
    package: str

    class Config:
        arbitrary_types_allowed = True
    