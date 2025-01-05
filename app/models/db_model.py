from sqlmodel import Field, SQLModel
from pydantic import BaseModel

class URLShortenerBase(SQLModel):
    id: int | None = Field(default=None, primary_key=True)
    url_shortened: str | None = Field(index=True, default=None)

class URLShortener(URLShortenerBase, table=True):
    url_unshortened: str | None = Field(index=True)
    time_visited: int | None = Field(default=0, index=False)
    
class URLPublic(BaseModel):
    url_unshortened: str
    url_shortened: str

class URLShortenerCreate(BaseModel):
    url_unshortened: str

class InvalidURL(BaseModel):
    error: str