from fastapi import FastAPI
import requests
import redis
from datetime import timedelta

redis_client = redis.Redis(host='localhost',port=6378)

API = "https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number=1"
app = FastAPI()

@app.get("/")
def root():
    return {"msg":"Application Running!!!"}

@app.get("/facts")
def facts():
    data = redis_client.get("fact")

    if data is None:
        res = requests.get(API)
        data = res.content
        redis_client.set("fact", data)
        redis_client.expire("fact", timedelta(seconds=10))
        
    return data

