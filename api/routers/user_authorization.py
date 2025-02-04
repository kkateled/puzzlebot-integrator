import logging
from typing import List
from fastapi import APIRouter, Depends, Security, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session
from api.auth import auth_handler, get_session_user
from api.db import get_db, crud, schemas
from api.db.models import UserAuthorization

router = APIRouter()
security = HTTPBearer()


@router.get(
    "/users/all",
    tags=["users"],
    response_model=List[schemas.UserAuthorizationResponse],
)
def all_users(
        db: Session = Depends(get_db),
        credentials: HTTPAuthorizationCredentials = Security(security)
):
    session_user = get_session_user(credentials, crud, db)
    return crud.get_all_users(db)


@router.post('/sugnup')
def signup(user_details: schemas.UserAuthorizationRequest, db: Session = Depends(get_db)):
    if crud.get(db, user_details.identificator) is not None:
        raise HTTPException(status_code=400, detail='Account already exists')
    hashed_password = auth_handler.encode_password(user_details.password)
    user = UserAuthorization(identificator=user_details.identificator,
                             password=hashed_password,
                             user_type=user_details.user_type,
                             enabled=True)
    try:
        db.add(user)
    except Exception as error:
        logging.exception(error)
        raise HTTPException(status_code=500, detail='Failed to signup user')
    else:
        db.commit()
        return schemas.UserAuthorizationResponse.from_orm(user)


@router.post('/login')
def login(user_details: schemas.UserAuthorizationRequest, db: Session = Depends(get_db)):
    user = crud.get(db, user_details.identificator)
    if user is None:
        raise HTTPException(status_code=401, detail='Invalid password or username')
    if not auth_handler.verify_password(user_details.password, user.password):
        raise HTTPException(status_code=401, detail='Invalid password or username')
    if user.access_token is not None or user.refresh_token is not None:
        raise HTTPException(status_code=401, detail='User already login')
    access_token = auth_handler.encode_token(user.identificator)
    refresh_token = auth_handler.encode_refresh_token(user.identificator)
    user.access_token = access_token
    user.refresh_token = refresh_token
    db.commit()
    return {'access_token': access_token, 'refresh_token': refresh_token}


@router.get('/refresh_token')
def refresh_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    refresh_token = credentials.credentials
    new_token = auth_handler.refresh_token(refresh_token)
    return {'access_token': new_token}


@router.get('/get-user/')
def get_user(identificator: str, db: Session = Depends(get_db)):
    db_user = crud.get(db, identificator=identificator)
    if db_user is None:
        raise HTTPException(status_code=401, detail='User not found')
    return db_user
