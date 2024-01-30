from fastapi import FastAPI, Path, Query
from datetime import datetime
from pymongo import MongoClient

app = FastAPI()

mongo_host = 'mongo'
mongo_port = 27017
mongo_db = 'turbit'

client = MongoClient(mongo_host, mongo_port)
db = client[mongo_db]

def retrieve_data(query):
    turbines = db['turbines_data']
    data = []
    for item_data in turbines.find(query):
        del item_data['_id']
        data.append(item_data)
    return data

@app.get("/")
def index():
    return {"Task": "Time Series Data Handling and API Development"}

@app.get("/turbines/{turbineId}")
def turbines(
        turbineId: int = Path(..., title="Turbine ID"),
        start_date: datetime = Query(..., title="Start date and time in ISO format"),
        end_date: datetime = Query(..., title="End date and time in ISO format")
        ):
    query = {"turbineId": turbineId, "Dat/Zeit": {"$gte": start_date, "$lte": end_date}}
    return retrieve_data(query)
