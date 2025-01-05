from sqlmodel import select
from models.db_model import URLShortener


def get_link(link, session):

    stmt = select(URLShortener).where(URLShortener.url_shortened == link)
    res = session.exec(stmt).first()

    if res:
        time_visited = res.time_visited + 1 if res.time_visited else 1
        res.time_visited = time_visited
        session.add(res)
        session.commit()
        session.refresh(res)

        return res.url_unshortened
    return "/notfound/"
