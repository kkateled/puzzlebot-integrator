from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import logging
from api.db import get_db, crud, schemas
from api.utils.converters import to_model

router = APIRouter()


@router.get(
    "/any_message/all",
    tags=["any_message"],
    response_model=List[schemas.AnyMessageResponse],
)
def any_message(
        page: int = 1,
        limit: int = 10,
        db: Session = Depends(get_db),
):
    return crud.get_all_any_message(db, page, limit)


@router.post('/any_message',
             response_model=schemas.AnyMessageResponse)
def add_message(message: schemas.AnyMessageRequest, db: Session = Depends(get_db)):
    try:
        return crud.save_any_message(db, to_model(message))
    except BaseException as error:
        logging.error(error)
        raise HTTPException(status_code=500, detail='Internal exception')
