from sqlalchemy.orm import Session
from api.db import models


def get_all_any_message(db: Session, page: int = 1, limit: int = 10):
    return (
        db.query(models.AnyMessage)
        .order_by(models.AnyMessage.date)
        .offset((page - 1) * limit)
        .limit(limit)
        .all()
    )


def get_all_users(db: Session):
    return (
        db.query(models.UserAuthorization)
        .order_by(models.UserAuthorization.id)
        .all()
    )


def get(db, identificator):
    return (
        db.query(models.UserAuthorization)
        .where(models.UserAuthorization.identificator == identificator)
        .order_by(models.UserAuthorization.id)
        .first()
    )
