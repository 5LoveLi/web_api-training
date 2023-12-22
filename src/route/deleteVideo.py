from fastapi import Depends, HTTPException, File, Form
from sqlalchemy.orm import Session
from typing import Annotated

from main import app, get_db, oauth2_scheme
from src.CRUD import videoCrud, userCrud
# from src.storage.minioStorage import upload_video_minio, upload_preview_minio



@app.delete("/video/{video_id}/delete")
async def delete_file(video_id: int, token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)):
    user_id = userCrud.get_current_user(db, token).id
    db_video = videoCrud.get_video_by_id(db, video_id)


    if db_video.id_author != user_id:
        raise HTTPException(
            status_code=400, detail="Вы не являетесь автором видео и не можете его удалить")

    return videoCrud.delete_video(db, db_video.id)