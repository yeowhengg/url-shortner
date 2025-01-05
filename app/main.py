from fastapi import FastAPI, Query, HTTPException
from contextlib import asynccontextmanager
from database import db_session
from routers import url, redirection, not_found, get_clicks


SessionDep = db_session.SessionDep


@asynccontextmanager
async def lifespan(app: FastAPI):
    db_session.create_db_and_tables()
    yield


tag_metadata = [
    {"name": "data", "description": "get your data endpoint"},
    {"name": "route_not_found", "description": "shortened route doesnt exist"},
    {"name": "redirection", "description": "redirection shorten link to original link"},
    {"name": "url_tools", "description": "main functionality of the urls"},
]
app = FastAPI(lifespan=lifespan)


app.include_router(url.router)
app.include_router(redirection.router)
app.include_router(not_found.router)
app.include_router(get_clicks.router)


@app.get("/")
def root():
    return "Navigate to /docs to find out more"


@app.get("/home")
def read_root():
    return {"Hello": "World"}
