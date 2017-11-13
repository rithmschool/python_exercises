"""empty message

Revision ID: c8e362388315
Revises: 2b5ead4151e6
Create Date: 2017-08-30 17:53:56.276445

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8e362388315'
down_revision = '2b5ead4151e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.Text(), nullable=True))
    op.create_unique_constraint(None, 'users', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.drop_column('users', 'password')
    # ### end Alembic commands ###
