from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

mongo_host = 'mongo'
mongo_port = 27017
mongo_db = 'turbit'

client = MongoClient(mongo_host, mongo_port)
db = client[mongo_db]

def retrieve_data():
    turbines = db['turbines_data']
    data = []
    for item_data in turbines.find():
        del item_data['_id']
        data.append(item_data)
        print("AAAA")
    print(data)    
    return data

@app.get("/")
def index():
    return {"Task": "Time Series Data Handling and API Development"}

@app.get("/retrieve_data")
def turbines():
    return retrieve_data()
