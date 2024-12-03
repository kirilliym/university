"""add_new_tables

Revision ID: 81bfe00bee9a
Revises: 9d09e1cb9b76
Create Date: 2024-10-28 08:51:10.801391

"""
from alembic import op
import sqlalchemy as sa

from project.core.config import settings


# revision identifiers, used by Alembic.
revision = '81bfe00bee9a'
down_revision = '9d09e1cb9b76'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('studies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String().with_variant(sa.String(length=255), 'postgresql'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema=settings.POSTGRES_SCHEMA
    )
    op.create_table('user_marks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mark', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('study_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['study_id'], ['university.studies.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['university.users.id'], onupdate='CASCADE', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    schema=settings.POSTGRES_SCHEMA
    )


def downgrade():
    op.drop_table('user_marks', schema=settings.POSTGRES_SCHEMA)
    op.drop_table('studies', schema=settings.POSTGRES_SCHEMA)