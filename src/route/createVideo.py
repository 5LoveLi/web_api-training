import json


from fastapi import Depends, HTTPException, File, Form
from sqlalchemy.orm import Session
from typing import Annotated

from main import app, get_db, oauth2_scheme
from src.CRUD import videoCrud, userCrud
from src.storage.minioStorage import upload_video_minio, upload_preview_minio



@app.post("/video/upload")
async def upload_file(token: Annotated[str, Depends(oauth2_scheme)], file_video: bytes = File(...), file_preview: bytes = File(...), json_data: str = Form(...), db: Session = Depends(get_db)):
    
    data_dict = json.loads(json_data)
    name_file = data_dict['name']
  
    user = userCrud.get_current_user(db, token)

    path_video = upload_video_minio(file_video, name_file)
    path_preview = upload_preview_minio(file_preview, name_file)

    db_video = videoCrud.get_video_by_name(db, name=name_file)

    if db_video:
        raise HTTPException(
            status_code=400, detail="Уже есть видео с таким названием")

    return videoCrud.create_video(db=db, video_name=name_file, video_description=data_dict['description'], id_author=user.id, preview = path_preview, video_link=path_video)