# FastAPI
## main.py
### Connection
Connects with mongoDB server using pymongo.
### Function definition
- `retrieve_data(query)`: Retrieves data from the data base and exposes it based on the query.
### Endpoints
#### `/turbine-stats`
Allows the retrieval of data based on optional parameters:
- `turbine_id`
- `start_date`
- `end_date` 
