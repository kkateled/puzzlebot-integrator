from pydantic import BaseModel, validator
from typing import Optional, Union
import datetime


class Bot(BaseModel):
    id: str
    username: str
    first_name: str


class Chat(BaseModel):
    id: str
    type: str
    first_name: Optional[str]
    title: Optional[str]
    username: str
    member_count: int

    @validator("type")
    def validate_type(cls, value: str) -> str:
        allowed_values = ["private", "channel", "group", "supergroup"]
        if value not in allowed_values:
            raise ValueError("Invalid value. Admissible values: private, channel, group, supergroup.")
        return value


class User(BaseModel):
    id: str
    first_name: str
    last_name: str
    username: str
    is_bot: bool
    category_name: str


class Command(BaseModel):
    name: str
    group_name: str
    call_type: str

    @validator("call_type")
    def validate_call_type(cls, value: str) -> str:
        allowed_values = ["reply", "inline"]
        if value not in allowed_values:
            raise ValueError("Invalid value. Admissible values: reply, inline.")
        return value


class Forms(BaseModel):
    name: str
    input_type: str
    block_type: Optional[str]
    type_: Optional[str]
    variable: str
    answer: str
    caption: Optional[str]
    file_ids: str

    @validator("input_type")
    def validate_input_type(cls, input_type: str) -> str:
        allowed_values = ["options", "exam", "message", "request_contact", "request_location"]
        if input_type not in allowed_values:
            raise ValueError("Invalid value.")
        return input_type

    @validator("block_type")
    def validate_block_type(cls, block_type, values, **kwargs) -> str:
        allowed_values = ["normal", "telegram"]
        input_type = values['input_type']
        if (block_type not in allowed_values) or (input_type not in ["options", "exam"]):
            raise ValueError("Invalid value.")
        return block_type

    @validator("type_")
    def validate_type_(cls, type_, values, **kwargs) -> str:
        input_type = values['input_type']
        if input_type != "message":
            raise ValueError("Invalid value.")
        return type_


class InvitedBy(BaseModel):
    id: str
    first_name: str
    last_name: str
    username: str


class Link(BaseModel):
    invited_by: Optional[InvitedBy]
    key: str
    type_: str

    @validator("type_", allow_reuse=True)
    def validate_type(cls, value: str) -> str:
        allowed_values = ["multiple", "promo", "referal"]
        if value not in allowed_values:
            raise ValueError("Invalid value.")
        return value

    @validator("invited_by", allow_reuse=True)
    def validate_type(cls, invited_by, values, **kwargs):
        type_ = values['type_']
        if type_ != "referal":
            raise ValueError("Invalid value.")
        return invited_by


class Text(BaseModel):
    text: str


class TypeNotification(BaseModel):
    type_notification: str


class Payment(BaseModel):
    sum: Union[int, float]
    name: str
    status: str

    @validator("status")
    def validate_type(cls, value: str) -> str:
        allowed_values = ["ok", "failed"]
        if value not in allowed_values:
            raise ValueError("Invalid value.")
        return value


class AnyMessage(BaseModel):
    date: float
    bot: Bot
    chat: Chat
    user: User
    message: str
    type_subscribe_event: str
    name: str

    @validator("type_subscribe_event")
    def validate_type_subscribe_event(cls, value: str) -> str:
        if value != "any_message":
            raise ValueError("Invalid value.")
        return value

    @validator("date")
    def parse_date(cls, value):
        return datetime.datetime.fromtimestamp(value).isoformat()


class CallCommand(BaseModel):
    date: float
    bot: Bot
    chat: Chat
    user: User
    command: Command
    type_subscribe_event: str
    name: str

    @validator("type_subscribe_event")
    def validate_type_subscribe_event(cls, value: str) -> str:
        if value != "call_command" or value != "call_command_from_group":
            raise ValueError("Invalid value.")
        return value

    @validator("date")
    def parse_date(cls, value):
        return str(value)


class FormAnswers(BaseModel):
    date: float
    bot: Bot
    chat: Chat
    user: User
    type_subscribe_event: str
    name: str
    forms: Forms

    @validator("type_subscribe_event")
    def validate_type_subscribe_event(cls, value: str) -> str:
        if value != "form_answers" or value != "custom_form_answers":
            raise ValueError("Invalid value.")
        return value

    @validator("date")
    def parse_date(cls, value):
        return str(value)


class NewMember(BaseModel):
    date: float
    bot: Bot
    chat: Chat
    user: User
    type_subscribe_event: str
    name: str

    @validator("type_subscribe_event")
    def validate_type_subscribe_event(cls, value: str) -> str:
        if value != "new_member" or value != "left_member":
            raise ValueError("Invalid value.")
        return value

    @validator("date")
    def parse_date(cls, value):
        return str(value)


class ActivateLink(BaseModel):
    date: float
    bot: Bot
    chat: Chat
    user: User
    link: Link
    type_subscribe_event: str
    name: str

    @validator("type_subscribe_event")
    def validate_type_subscribe_event(cls, value: str) -> str:
        if value != "activate_link":
            raise ValueError("Invalid value.")
        return value

    @validator("date")
    def parse_date(cls, value):
        return str(value)

