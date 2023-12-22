from fastapi import Depends
from sqlalchemy.orm import Session
from typing import Annotated

from main import app, get_db, oauth2_scheme
from src.CRUD import userCrud, likeCrud


@app.post('/video/{video_id}/like')
async def viewing_video(video_id: int, token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)):
    user_id = userCrud.get_current_user(db, token).id
    user_liked = likeCrud.user_like_video(db=db, video_id=video_id, user_id=user_id)
    if user_liked:
        likes = likeCrud.delete_like_user(db=db, video_id=video_id, user_id=user_id)
        return {'likes': likes}
    else:
        likes = likeCrud.create_like(db=db, video_id=video_id, user_id=user_id)
        return {'likes': likes}