from fastapi import APIRouter, HTTPException
from database import db_session
from models.db_model import LinkClicks
from helper import get_data

SessionDep = db_session.SessionDep

router = APIRouter(prefix="/data", tags=["data"])


@router.get("/")
def clicks_root():
    return "endpoint is to fetch clicks"


@router.get("/clicks", response_model=LinkClicks)
def get_clicks(session: SessionDep, shortened_link):
    data = get_data.clicks(session, shortened_link)

    if not data:
        raise HTTPException(status_code=400, detail="url is not valid")

    return data
