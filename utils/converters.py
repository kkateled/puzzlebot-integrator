from utils.metadata import AnyMessage


def to_model(message: AnyMessage):
    dict_chat = change_name_key(message.chat.dict(), "chat_")
    dict_user = change_name_key(message.user.dict(), "user_")

    new_dict = message.dict()
    new_dict.pop('user')
    new_dict.pop('chat')
    new_dict.update(dict_chat)
    new_dict.update(dict_user)

    return new_dict


def change_name_key(source: dict, add_name: str) -> dict:
    new_dict = {}
    for old_key in source.keys():
        new_key = add_name + old_key
        new_dict[new_key] = source[old_key]
    return new_dict

