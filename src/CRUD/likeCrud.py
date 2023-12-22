from sqlalchemy.orm import Session
from datetime import datetime

from src.model.like import Like
from src.schema.likeSchema import LikeCreate


def get_all_likes_video(db: Session, video_id: int):
    return len(db.query(Like).filter(Like.id_video == video_id).all())


def get_all_video_like_user(db: Session, user_id: int):
    return db.query(Like).filter(Like.id_user == user_id).all()


def user_like_video(db: Session, video_id: int, user_id: int):
    return db.query(Like).filter(Like.id_video == video_id, Like.id_user == user_id).first()

def delete_like_user(db: Session, video_id: int, user_id: int):
    like = db.query(Like).filter(Like.id_video == video_id, Like.id_user == user_id).first()
    db.delete(like)
    db.commit()
    # db.refresh(like)
    return get_all_likes_video(db=db, video_id=video_id)


def create_like(db: Session, video_id: int, user_id: int):
    db_like = Like(id_video=video_id, id_user=user_id)
    db.add(db_like)
    db.commit()
    db.refresh(db_like)
    return get_all_likes_video(db=db, video_id=video_id)