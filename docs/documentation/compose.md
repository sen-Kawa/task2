# compose.yaml
## Services
### mongo
Built from [mongo](https://hub.docker.com/_/mongo/) Docker Official Image.
### data_retrieval
Built based on the [Dockerfile](../../data_retrieval_script/Dockerfile)
#### Dockerfile 
- Builds from the official Python base image. 
- Installs python libraries: requests and pymongo.
- Copies the script into the container.
- Gives exectuting rights to the script.
- Runs the script.
### fastapi
Built based on the [Dockerfile](../../fastapi/Dockerfile)
#### Dockerfile 
- Builds from [image](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker)
- Copies the app directory
- Installs python library pymongo
- Exposes port 8000

