"""store item picture

Revision ID: 4ac7a0b69c34
Revises: d72106f78e8d
Create Date: 2020-05-13 16:20:55.278270

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4ac7a0b69c34'
down_revision = 'd72106f78e8d'
branch_labels = None
depends_on = None


def upgrade():
    #op.create_table(
    #    'pictureicon'
    #    ,sa.Column('id', sa.String, primary_key=True)
        #,sa.Column('weapon_id', sa.String, sa.ForeignKey('weapon.id'))
    #    ,sa.Column('url', sa.String)
    #    ,sa.Column('pictureBinary', sa.Binary)
    #    )

    #op.add_column(
    #    'weapon'
    #    ,sa.Column('pictureicon_id', sa.String, sa.ForeignKey('pictureicon.id') )
    #)
    pass


def downgrade():
    #op.drop_table('pictureicon')
    #op.drop_column('weapon', 'pictureicon_id')
    pass
