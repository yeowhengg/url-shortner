from fastapi import APIRouter, Response
from fastapi.responses import RedirectResponse
from database import db_session
from helper import check_link

SessionDep = db_session.SessionDep

router = APIRouter(prefix="/notfound", tags=["route_not_found"])


@router.get("/")
def redirect_route():
    return "Not Found..."
