"""user login is unique and pk now

Revision ID: 78e076e64a2b
Revises: 1f0e2170bd92
Create Date: 2024-12-04 18:29:47.468877

"""
from alembic import op
import sqlalchemy as sa

from project.core.config import settings


# revision identifiers, used by Alembic.
revision = '78e076e64a2b'
down_revision = '1f0e2170bd92'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'users', ['login'], schema='university')
    op.drop_column('users', 'id', schema='university')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False), schema='university')
    op.drop_constraint(None, 'users', schema='university', type_='unique')
    # ### end Alembic commands ###