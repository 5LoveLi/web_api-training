from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer

from src.model import user, video, like
from src.database import SessionLocal, engine


user.Base.metadata.create_all(bind=engine)
video.Base.metadata.create_all(bind=engine)
like.Base.metadata.create_all(bind=engine)


app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



from src.route import tape, registration, authorizations, likeVideo, viewing, createVideo, deleteVideo, likeVideoWebsoket


if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
