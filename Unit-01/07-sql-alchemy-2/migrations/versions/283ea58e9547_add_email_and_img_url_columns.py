"""add email and img_url columns

Revision ID: 283ea58e9547
Revises: 9733aa9eabb6
Create Date: 2017-08-26 17:48:28.672230

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '283ea58e9547'
down_revision = '9733aa9eabb6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.Text(), nullable=True))
    op.add_column('users', sa.Column('img_url', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'img_url')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###
