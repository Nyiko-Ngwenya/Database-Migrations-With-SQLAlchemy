"""Create migrations to change chatname to rocketchat

Revision ID: 7bb2e6fc8f49
Revises: 61cbff913916
Create Date: 2020-10-14 15:05:38.995540

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7bb2e6fc8f49'
down_revision = '61cbff913916'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('recruits', 'chatname', nullable=True,new_column_name='rocketchat_user')
    # op.drop_column('recruits', 'chatname')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recruits', sa.Column('chatname', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('recruits', 'rocketchat_user')
    # ### end Alembic commands ###
