from fastapi import FastAPI, Query, HTTPException
from contextlib import asynccontextmanager
from .database import db_session
from .routers import url

SessionDep = db_session.SessionDep

@asynccontextmanager
async def lifespan(app: FastAPI):
    db_session.create_db_and_tables()
    yield

app = FastAPI(lifespan=
              lifespan)


app.include_router(url.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}

