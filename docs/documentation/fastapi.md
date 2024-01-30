# FastAPI
## main.py
### Connection
Connects with mongoDB server using pymongo.
### Function definition
- `retrieve_data(turbineId)` retrieves data from the data base and exposes it based on the query.
### Routes
- `turbines/{turbineId}` allows the retrieval of data based on turbine id and time ranges.
