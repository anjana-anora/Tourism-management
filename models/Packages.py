from pydantic import BaseModel
from datetime import datetime

class Packages(BaseModel):
    name: str
    start : datetime
    days: int
    price: float
    rating: float = 0
