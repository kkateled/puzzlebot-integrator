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


"""
select * from any_message
order by date
offset 4
limit 6
"""

"1 2 3 4 5 6 7 8 9 10"
# offset = 0 limit = 2 -> "1 2"
# offset = 4 limit = 2 -> "5 6"
