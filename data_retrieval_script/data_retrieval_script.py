import requests
import csv
from datetime import datetime
from io import StringIO
from pymongo import MongoClient

mongo_host='mongo'
mongo_port=27017
mongo_db='turbit'

client = MongoClient(mongo_host, mongo_port)
db = client[mongo_db]
turbines = db['turbines_data']

def fetch_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.text
    else:
        print("Failed to fetch data.")
        return None

def store_data(turbine_id, data):
    if (data):
        csv_reader = csv.DictReader(StringIO(data), fieldnames=None, delimiter=';', skipinitialspace=True)
        next(csv_reader, None)
        newData = []
        for item in csv_reader:
            item["Dat/Zeit"] = datetime.strptime(item["Dat/Zeit"], "%d.%m.%Y, %H:%M")
            item["turbineId"] = turbine_id
            newData.append(item)
            
        result = turbines.insert_many(newData)
        
        print("Data stored succesfully.")
    else:
        print("No data to store.")

api_map = {
        1: 'https://nextcloud.turbit.com/s/GTbSwKkMnFrKC7A/download/Turbine1.csv',
        2: 'https://nextcloud.turbit.com/s/G3bwdkrXx6Kmxs3/download/Turbine2.csv'
}

for turbine_id, api_url in api_map.items():
    api_data = fetch_data(api_url)
    store_data(turbine_id, api_data)

client.close()

print('SCRIPT RUN')
