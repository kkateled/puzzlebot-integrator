from pydantic import BaseModel


class AnyMessage(BaseModel):
    user_id: str
    user_username: str
    chat_username: str
    message: str
    chat_title: str
    date: str

    class Config:
        orm_mode = True
