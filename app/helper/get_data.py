from sqlmodel import select
from models.db_model import URLShortener


def clicks(session, shortened_link):
    stmt = select(URLShortener).where(URLShortener.url_shortened == shortened_link)
    res = session.exec(stmt).first()

    if res:
        return {
            "url_unshortened": res.url_unshortened,
            "url_shortened": res.url_shortened,
            "clicks": res.time_visited,
        }

    return False
