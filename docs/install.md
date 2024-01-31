# Installation instructions
## Install
```
git clone https://github.com/sen-Kawa/task2.git
```
### Build and Run
```
docker compose up --build
```

Access FastAPI in your browser `0.0.0.0:8000/docs`

Query data with turbine id and date/time ranges in ISO format  

`http://0.0.0.0:8000/turbine-stats/?turbine_id={ID}&start_date=YYYY-MM-DDTHH:MM:SS&end_date=YYYY-MM-DDTHH:MM:SS`

**Examples:**
```
http://0.0.0.0:8000/turbine-stats
```
```
http://0.0.0.0:8000/turbine-stats/?turbine_id=1
```
```
http://0.0.0.0:8000/turbine-stats/?turbine_id=1&start_date=2016-01-26T00:00:00
```
```
http://0.0.0.0:8000/turbine-stats/?start_date=2016-01-26T00:00:00
```
```
http://0.0.0.0:8000/turbine-stats/?turbine_id=1&start_date=2016-01-26T00:00:00&end_date=2016-01-27T23:49:59
```
### To interact with MongoDB
```
docker compose up --build -d
```
Execute an interactive shell in the container:
```
docker exec -it mongodb bash
```
Use MongoDB shell `mongosh`.
To view the databases type `show dbs`, to view the collections `show collections` and to view the desired data type `db.[collection name].find()`

[mongosh CRUD Operations Documentation](https://www.mongodb.com/docs/mongodb-shell/crud/)
