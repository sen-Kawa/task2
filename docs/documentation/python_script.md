# Python Script Documentation
## Overview
This Python script fetches turbine data from two endpoints and stores it in one single collection within a defined MongoDB database.

### Libraries
- **requests** is used for the API requests.
- **pymongo** is used to interact with MongoDB.
- **datetime** is used to convert the date string into a python datetime object.
- **csv** is used to read the CSV file.
- **io** is used to read the CSV data as a file.

### Functions
- `fetch_data(api_url)` sends a GET request to the specified endpoint in the parameter.
- `store_data(turbine_id, data)` creates a dictionary from the CSV, uses the header as fieldnames, sets the delimiter as `;`. Converts the value of `Dat/Zeit` key into a python datetime object, adds the turbineId key and stores into a MongoDB collection.

### API Mapping
`api_map` is a dictionary that maps the API endpoints to turbine id.
