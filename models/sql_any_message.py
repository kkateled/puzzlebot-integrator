import sqlalchemy as db

engine = db.create_engine('sqlite:///any_message.db')
metadata = db.MetaData()

any_message_table = db.Table(
    "any_message",
    metadata,
    db.Column("date", db.String()),
    db.Column("chat_id", db.String()),
    db.Column("chat_type", db.String(15)),
    db.Column("chat_first_name", db.String(50)),
    db.Column("chat_title", db.String(100)),
    db.Column("chat_username", db.String(50)),
    db.Column("chat_member_count", db.Integer()),
    db.Column("user_id", db.String()),
    db.Column("user_first_name", db.String(50)),
    db.Column("user_last_name", db.String(50)),
    db.Column("user_username", db.String(50)),
    db.Column("user_is_bot", db.Boolean),
    db.Column("user_category_name", db.String(80)),
    db.Column("message", db.String()),
    db.Column("type_subscribe_event", db.String(30)),
    db.Column("name", db.String(50))
)

metadata.create_all(engine)
