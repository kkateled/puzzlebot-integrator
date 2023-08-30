from sqlalchemy import Column, Integer, String, Boolean
from api.db import Base


class AnyMessage(Base):
    __tablename__ = "any_message"

    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, index=True)
    date = Column(String)
    chat_id = Column(String, index=True)
    chat_type = Column(String)
    chat_first_name = Column(String)
    chat_title = Column(String)
    chat_username = Column(String)
    chat_member_count = Column(Integer)
    user_first_name = Column(String)
    user_last_name = Column(String)
    user_username = Column(String)
    user_is_bot = Column(Boolean)
    user_category_name = Column(String)
    message = Column(String)
    type_subscribe_event = Column(String)
    name = Column(String)


class UserAuthorization(Base):
    __tablename__ = "user_authorization"

    id = Column(Integer, primary_key=True, index=True)
    identificator = Column(String)
    password = Column(String)
    user_type = Column(String)
    access_token = Column(String)
    refresh_token = Column(String)
    enabled = Column(String)

