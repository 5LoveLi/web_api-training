from fastapi import Depends
from sqlalchemy.orm import Session

from main import app, get_db
from src.CRUD import videoCrud, userCrud, likeCrud
from src.schema.videoSchema import Video


@app.get('/video/{video_id}')
def viewing_video(video_id, db: Session = Depends(get_db)):
    video_db = videoCrud.get_video_by_id(db=db, id=video_id)
    likes = likeCrud.get_all_likes_video(db=db, video_id=video_id)
    author_name = userCrud.get_user(db=db, user_id=video_db.id_author).login
    video = Video(id=video_db.id, name=video_db.name, author=author_name, like=likes, description=video_db.description, data=video_db.data, link=video_db.link)
    return video