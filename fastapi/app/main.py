from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

mongo_host = 'mongo'
mongo_port = 27017
mongo_db = 'turbit'

client = MongoClient(mongo_host, mongo_port)
db = client[mongo_db]

def retrieve_data(turbineId: int):
    turbines = db['turbines_data']
    data = []
    for item_data in turbines.find({"turbineId": turbineId}):
        del item_data['_id']
        data.append(item_data)
    return data

@app.get("/")
def index():
    return {"Task": "Time Series Data Handling and API Development"}

@app.get("/turbines/{turbineId}")
def turbines(turbineId: int):
    return retrieve_data(turbineId)
