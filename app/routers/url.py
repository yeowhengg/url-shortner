from fastapi import APIRouter
from sqlmodel import select
from ..models.db_model import URLPublic, URLShortenerBase, URLShortenerCreate, URLShortener
from ..database import db_session
from ..helper import generate_link

SessionDep = db_session.SessionDep

router = APIRouter (
    prefix="/url",
)

@router.get("/")
def test_route():
    return "Hello world!"

@router.get("/allurl")
def retrieve_url(session: SessionDep) -> list[URLShortener]:
    url = session.exec(select(URLShortener)).all()
    return url

@router.post("/shortener/")
def url_shortener(session: SessionDep, url: URLShortenerCreate):
    db_url = URLShortener.model_validate(url)
    new_url = generate_link.to_shorten(url.url_unshortened)
    db_url.url_shortened = new_url
    session.add(db_url)
    session.commit()
    session.refresh(db_url)
    return {"url_unshortened": url.url_unshortened,
    "url_shortened": new_url}
