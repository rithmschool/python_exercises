"""empty message

Revision ID: 224bed95b98e
Revises: 
Create Date: 2017-08-18 17:15:40.641239

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '224bed95b98e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('snacks', sa.Column('calories', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('snacks', 'calories')
    # ### end Alembic commands ###
