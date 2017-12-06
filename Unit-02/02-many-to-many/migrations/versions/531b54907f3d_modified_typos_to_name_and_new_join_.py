"""modified typos to name and new join table name

Revision ID: 531b54907f3d
Revises: 24224d51ad8d
Create Date: 2017-12-05 20:15:17.867706

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '531b54907f3d'
down_revision = '24224d51ad8d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employees_departments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('department_id', sa.Integer(), nullable=True),
    sa.Column('employee_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('employee_departments')
    op.add_column('departments', sa.Column('name', sa.Text(), nullable=True))
    op.drop_column('departments', 'department_name')
    op.add_column('employees', sa.Column('name', sa.Text(), nullable=True))
    op.drop_column('employees', 'employee_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employees', sa.Column('employee_name', sa.TEXT(), autoincrement=False, nullable=True))
    op.drop_column('employees', 'name')
    op.add_column('departments', sa.Column('department_name', sa.TEXT(), autoincrement=False, nullable=True))
    op.drop_column('departments', 'name')
    op.create_table('employee_departments',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('department_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('employee_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['department_id'], ['departments.id'], name='employee_departments_department_id_fkey', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['employee_id'], ['employees.id'], name='employee_departments_employee_id_fkey', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name='employee_departments_pkey')
    )
    op.drop_table('employees_departments')
    # ### end Alembic commands ###
