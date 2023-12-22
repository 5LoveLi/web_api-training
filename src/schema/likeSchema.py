from pydantic import BaseModel


class LikeBase(BaseModel):
    id_video: int
    id_user: int


class LikeCreate(LikeBase):
    pass


class Like(LikeBase):
    id: int