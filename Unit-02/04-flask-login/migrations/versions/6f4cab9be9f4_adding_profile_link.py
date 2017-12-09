"""adding profile link

Revision ID: 6f4cab9be9f4
Revises: 02c5024ca366
Create Date: 2017-12-03 20:54:31.115296

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f4cab9be9f4'
down_revision = '02c5024ca366'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('profile_link', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profile_link')
    # ### end Alembic commands ###
