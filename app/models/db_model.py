from sqlmodel import Field, SQLModel

class URLShortenerBase(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    url_shortened: str | None = Field(index=True, default=None)

class URLShortener(URLShortenerBase, table=True):
    url_unshortened: str | None = Field(index=True)
    time_visited: int | None = Field(default=None, index=False)
    
class URLPublic(URLShortenerBase):
    url_unshortened: str
    url_shortened: str

class URLShortenerCreate(URLShortenerBase):
    url_unshortened: str