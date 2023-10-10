"""user authorization

Revision ID: 5f2588b801da
Revises: 34d413f2378b
Create Date: 2023-08-24 00:35:49.628361

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5f2588b801da'
down_revision: Union[str, None] = '34d413f2378b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "user_authorization",
        sa.Column("id", sa.BigInteger, primary_key=True, index=True, autoincrement=True),
        sa.Column("identificator", sa.String),
        sa.Column("password", sa.String),
        sa.Column("user_type", sa.String),
        sa.Column("access_token", sa.String),
        sa.Column("refresh_token", sa.String),
        sa.Column("enabled", sa.Boolean)
    )


def downgrade() -> None:
    op.drop_table("user_authorization")

