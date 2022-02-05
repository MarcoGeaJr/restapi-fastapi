# REST API with FastAPI
A REST API in Python with FastAPI and SQLAlchemy ORM

## Summary
The API can be use to consume SARS data from 2003. This return a list of dicts with data.
This Repo contains a "load.py" file that load the CSV data on a SQLite database call "sars.db". 

### Required Installs
- pip install sqlalchemy
- pip install pydantic
- pip install fastapi
- pip install uvicorn

### How to use
- Install required packages
- Run "load.py" file
- Run "uvicorn Main:app" in Kernel
- Be happy ;)
