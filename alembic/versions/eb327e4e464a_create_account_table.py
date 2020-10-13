"""create account table

Revision ID: eb327e4e464a
Revises: 
Create Date: 2020-10-13 21:46:29.341617

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb327e4e464a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'recruits',
        sa.Column('id', sa.Integer ,primary_key=True),
        sa.Column('first_name', sa.String(50)),
        sa.Column('surname', sa.String(50)),
        sa.Column('chatname', sa.String(50)),
        sa.Column('github_name', sa.String(50)),
        sa.Column('id_number', sa.Integer)
    )


def downgrade():
    op.drop_table("recruits")
