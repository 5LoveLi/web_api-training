from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Annotated

from main import app, get_db, oauth2_scheme
from src.CRUD import videoCrud, userCrud, likeCrud
from src.schema.videoSchema import VisitCard

router = APIRouter()

def correction_data(videos: list, db):
    tape = []
    for video in videos:
        author_name = userCrud.get_user(db=db, user_id=video.id_author).login
        author_name = ''
        likes = likeCrud.get_all_likes_video(db=db, video_id=video.id)
        card = VisitCard(id=video.id, name=video.name, author=author_name, preview=video.preview, like=likes)
        tape.append(card)
    return tape


@router.get('')
async def get_tape(db: Session = Depends(get_db)):
    videos = videoCrud.get_video(db)
    tape = correction_data(videos, db)
    return tape


@router.get('/search/{string_search}')
async def get(string_search:str, db: Session = Depends(get_db)):
    videos = videoCrud.get_video_by_name(db=db, name=string_search)
    tape = correction_data(videos, db)
    return tape


@router.get('/like')
async def get_tape_like(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)):
    user_id = userCrud.get_current_user(db, token).id
    videos = videoCrud.get_videos_by_like(db, user_id)
    tape = correction_data(videos, db)
    return tape


@router.get('/my')
async def get_my_tape(token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)):
    user_id = userCrud.get_current_user(db, token).id
    videos = videoCrud.get_my_create_videos(db, user_id)
    tape = correction_data(videos, db)
    return tape



app.include_router(router, prefix="/tape")