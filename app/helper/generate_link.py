from . import convert_base62, convert_base64

def to_shorten(link: str, session, new_url_class, row):
    base64 = convert_base64.str2int(link, row)
    db_url = new_url_class
    db_url.url_shortened = "http://127.0.0.1:8000/"+convert_base62.convertToBase62(base64, row)
    session.add(db_url)
    session.commit()
    session.refresh(db_url)
    
    return db_url.url_shortened