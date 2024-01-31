# FastAPI
## main.py
### Connection
Connects with mongoDB server using pymongo.
### Function definition
- `retrieve_data(query)`: Retrieves data from the data base and exposes it based on the query.
### Endpoints
#### `/turbine-stats`
Allows the retrieval of data based on optional url query parameters:
- `turbine_id` integer
- `start_date` ISO format date
- `end_date` ISO format date
