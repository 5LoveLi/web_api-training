from sqlalchemy import Column, Integer

from src.database import Base


class Like(Base):
    __tablename__ = "likes"

    id = Column(Integer, primary_key=True, index=True)
    id_video = Column(Integer)
    id_user = Column(Integer)