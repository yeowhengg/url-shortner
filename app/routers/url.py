from fastapi import APIRouter, HTTPException
from sqlmodel import select
from models.db_model import URLPublic, URLShortenerCreate, URLShortener, InvalidURL
from database import db_session
from helper import generate_link, valid_url

SessionDep = db_session.SessionDep

router = APIRouter(
    prefix="/url",
)


@router.get("/")
def test_route():
    return "Hello world!"


@router.get("/allurl")
def retrieve_url(session: SessionDep) -> list[URLShortener]:
    url = session.exec(select(URLShortener)).all()
    return url


@router.post(
    "/shortener/", responses={"200": {"model": URLPublic}, "400": {"model": InvalidURL}}
)
def url_shortener(session: SessionDep, url: URLShortenerCreate):
    db_url = URLShortener.model_validate(url)
    check_valid_url = valid_url.check_valid(db_url)

    if check_valid_url:
        row = len(session.exec(select(URLShortener))._allrows()) + 1

        new_url = generate_link.to_shorten(url.url_unshortened, session, db_url, row)

        return {"url_unshortened": url.url_unshortened, "url_shortened": new_url}

    raise HTTPException(status_code=400, detail="url is not valid")
