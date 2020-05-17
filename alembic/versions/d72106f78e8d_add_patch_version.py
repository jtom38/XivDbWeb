"""add patch version

Revision ID: d72106f78e8d
Revises: c9b7605de680
Create Date: 2020-05-09 15:58:53.446980

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd72106f78e8d'
down_revision = 'c9b7605de680'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('weapon', sa.Column('patch', sa.String))
    pass


def downgrade():
    op.drop_column('weapoon', 'patch')
    pass
