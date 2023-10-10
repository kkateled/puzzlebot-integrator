"""create anymessage table

Revision ID: 34d413f2378b
Revises: 
Create Date: 2023-08-20 20:04:24.342398

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '34d413f2378b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "any_message",
        sa.Column("id", sa.BigInteger, primary_key=True, index=True, autoincrement=True),
        sa.Column("user_id", sa.String, index=True),
        sa.Column("date", sa.String),
        sa.Column("chat_id", sa.String, index=True),
        sa.Column("chat_type", sa.String(15)),
        sa.Column("chat_first_name", sa.String(50)),
        sa.Column("chat_title", sa.String(100)),
        sa.Column("chat_username", sa.String(50)),
        sa.Column("chat_member_count", sa.BigInteger),
        sa.Column("user_first_name", sa.String(50)),
        sa.Column("user_last_name", sa.String(50)),
        sa.Column("user_username", sa.String(50)),
        sa.Column("user_is_bot", sa.Boolean),
        sa.Column("user_category_name", sa.String(80)),
        sa.Column("message", sa.String),
        sa.Column("type_subscribe_event", sa.String(30)),
        sa.Column("name", sa.String(50))
    )


def downgrade() -> None:
    op.drop_table("any_message")
