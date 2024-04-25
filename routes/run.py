from fastapi import APIRouter


run = APIRouter()


@run.get("/")
async def check_app_status():
    return {
        "status_code": 200,
        "message": "App is running"
    }