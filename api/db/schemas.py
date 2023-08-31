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


class UserAuthorizationResponse(BaseModel):
    id: int
    identificator: str
    user_type: str | None
    enabled: bool

    class Config:
        orm_mode = True


class UserAuthorizationRequest(BaseModel):
    identificator: str
    password: str
    user_type: str | None

    class Config:
        orm_mode = True
