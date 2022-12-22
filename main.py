from fastapi import FastAPI
import json
from model.user_page import UserPage
from model.recommend import Recommend

app = FastAPI()


@app.get("/api/user-page")
async def get_user_page(account):
    return json.loads(UserPage(account).to_json())


@app.get("/api/recommend")
async def get_recommend():
    return json.loads(Recommend().to_json())