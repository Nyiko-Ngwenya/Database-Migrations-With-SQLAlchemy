"""Added recruit email address to be unique also

Revision ID: f415547e0fba
Revises: 8bab4ed17853
Create Date: 2020-10-14 12:04:41.070022

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f415547e0fba'
down_revision = '8bab4ed17853'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'recruits', ['personal_email_address'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'recruits', type_='unique')
    # ### end Alembic commands ###
