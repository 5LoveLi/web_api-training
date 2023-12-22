from sqlalchemy.orm import Session
from datetime import datetime
from src.CRUD.likeCrud import get_all_video_like_user

from src.model.video import Video


def get_video(db: Session):
    return db.query(Video).all()

def get_video_by_id(db: Session, id:int) -> Video:
    return db.query(Video).filter(Video.id == id).first()


def get_video_by_name(db: Session, name: str):
    return db.query(Video).filter(Video.name == name).all()


def get_videos_by_like(db: Session, id_user: int): 
    likes = get_all_video_like_user(db=db, user_id=id_user)
    videos = []
    for like in likes:
        videos.append(get_video_by_id(db, like.id_video))

    return videos

def get_my_create_videos(db: Session, id_user: int):
    return db.query(Video).filter(Video.id_author==id_user)


def create_video(db: Session, video_name, video_description, id_author, preview, video_link):
    db_video = Video(
        name=video_name, description=video_description, data=datetime.now(), id_author=id_author, preview=preview, link=video_link
        )
    db.add(db_video)
    db.commit()
    db.refresh(db_video)
    return db_video

def delete_video(db: Session, id:int):
    video = db.query(Video).filter(Video.id == id).first()

    if video is not None:
        db.delete(video)
        db.commit()
        return {"message":"Видео удалено"}
    else:
        return "Видео с таким id нет"
