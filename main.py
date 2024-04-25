from fastapi import FastAPI
from routes.run import run
from routes.user import user
from db.databaseConnect import engine
from models import models


app = FastAPI()
models.Base.metadata.create_all(bind=engine)


app.include_router(run)
app.include_router(user)