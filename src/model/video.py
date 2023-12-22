from sqlalchemy import Column, Integer, String, DateTime

from src.database import Base


class Video(Base):
    __tablename__ = "videos"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    description = Column(String)
    data = Column(DateTime)
    id_author = Column(Integer)
    preview = Column(String)
    link = Column(String)
