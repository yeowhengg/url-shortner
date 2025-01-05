from fastapi import APIRouter, Response
from fastapi.responses import RedirectResponse
from ..database import db_session
from ..helper import check_link

SessionDep = db_session.SessionDep

router = APIRouter()

@router.get("/{shortcode}")
def redirect_route(shortcode: str, session: SessionDep):
    test = check_link.get_link("http://127.0.0.1:8000/"+shortcode, session)
    return RedirectResponse(url=test)