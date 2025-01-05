from fastapi import APIRouter, Response
from fastapi.responses import RedirectResponse
from ..database import db_session
from ..helper import check_link
import os
from dotenv import load_dotenv
load_dotenv()
os.getenv
DOMAIN_NAME = os.getenv('DOMAIN_NAME')

SessionDep = db_session.SessionDep

router = APIRouter()

@router.get("/{shortcode}")
def redirect_route(shortcode: str, session: SessionDep):
    test = check_link.get_link(f"{DOMAIN_NAME}"+shortcode, session)
    return RedirectResponse(url=test)