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
    for item_data in turbines.find(query).sort("Dat/Zeit"):
        del item_data['_id']
        data.append(item_data)
    return data

@app.get("/")
def index():
    return {"Task": "Time Series Data Handling and API Development"}

@app.get("/turbine-stats")
def turbines(
        turbine_id: int = Query(None, title="The turbine id"),
        start_date: datetime = Query(None, title="Start date and time in ISO format"),
        end_date: datetime = Query(None, title="End date and time in ISO format")
        ):
    
    query = {}
    if turbine_id is not None:
        query["turbineId"] = turbine_id
    if start_date:
        query["Dat/Zeit"] = {"$gte": start_date}
    if end_date:
        if query["Dat/Zeit"]:
            query["Dat/Zeit"]["$lte"] = end_date
        else:
            query["Dat/Zeit"] = {"$lte": end_date}

    return retrieve_data(query)
