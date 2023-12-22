from typing import Annotated

from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from werkzeug.security import check_password_hash, generate_password_hash

from src.route.authorizations import oauth2_scheme, SECRET_KEY, ALGORITHM

from src.model.user import User
from src.schema.userSchema import UserCreate
from src.schema.authSchema import TokenData


def get_user(db: Session, user_id: int) -> User:
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_login(db: Session, login: str) -> User:
    return db.query(User).filter(User.login == login).first()


def create_user(db: Session, user: UserCreate):
    db_user = User(
        login=user.login, hashed_password=generate_password_hash(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(db: Session, login: str, password: str):
    user = get_user_by_login(db, login)
    if not user:
        return False
    if not check_password_hash(user.hashed_password, password):
        return False
    return user


# дает текущего пользователя
def get_current_user(db: Session, token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user_by_login(db, login=token_data.username)
    if user is None:
        raise credentials_exception
    return user