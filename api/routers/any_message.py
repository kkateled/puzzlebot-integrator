from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.db import get_db, crud, schemas

router = APIRouter()


@router.get(
    "/any_message/all",
    tags=["any_message"],
    response_model=List[schemas.AnyMessage],
)
def any_message(
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    return crud.get_all_any_message(db, page, limit)
