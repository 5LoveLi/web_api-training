from datetime import datetime
from pydantic import BaseModel


class VideoBase(BaseModel):
    id: int
    name: str
    author: str
    like: int



class VisitCard(VideoBase):
    preview: str

    


class Video(VideoBase): 
    data: datetime 
    description: str | None = None
    link: str

    
    class Config:
        from_attributes = True 


class SearchBase(BaseModel):
    stringQuery: str
