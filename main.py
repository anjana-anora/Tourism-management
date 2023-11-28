from fastapi import FastAPI
from routes.packages import packages
from routes.passengers import passengers
import uvicorn

app = FastAPI()

app.include_router(packages, prefix='/packages',tags=['Packages'])
app.include_router(passengers, prefix='/passengers',tags=['Passengers'])

if __name__ =="__main__":
    uvicorn.run(app, host = '127.0.0.1', port=8000)
