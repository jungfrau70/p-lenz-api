"""create db and tables

Revision ID: 9e49e88d628b
Revises: 
Create Date: 2022-10-07 01:24:41.389310

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e49e88d628b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
        create table events (
            id bigserial primary key,
            name text,
            completed boolean not null default false
        )
    """)

def downgrade() -> None:
    op.execute("""
        drop table events;
    """)
