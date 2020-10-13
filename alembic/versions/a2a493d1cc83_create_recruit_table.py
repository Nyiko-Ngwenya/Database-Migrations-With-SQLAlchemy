"""create recruit table

Revision ID: a2a493d1cc83
Revises: 
Create Date: 2020-10-13 11:09:26.361428

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2a493d1cc83'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'recruits',
        sa.Column('id', sa.Integer ,primary_key=True),
        sa.Column('first_name', sa.String(50), nullable=False),
        sa.Column('surname', sa.String(50)),
        sa.Column('chatname', sa.String(50)),
        sa.Column('github_name', sa.String(50)),
        sa.Column('id_number', sa.Integer),
    )


def downgrade():
    op.drop_table("recruits")