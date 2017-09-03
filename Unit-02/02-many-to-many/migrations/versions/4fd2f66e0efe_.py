"""empty message

Revision ID: 4fd2f66e0efe
Revises: 8c7da54d84fd
Create Date: 2017-09-01 07:26:49.903758

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4fd2f66e0efe'
down_revision = '8c7da54d84fd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('message', sa.Text(), nullable=True))
    op.drop_column('messages', 'messages')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('messages', sa.TEXT(), autoincrement=False, nullable=True))
    op.drop_column('messages', 'message')
    # ### end Alembic commands ###
