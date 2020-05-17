"""fresh start

Revision ID: c9b7605de680
Revises: 
Create Date: 2020-04-26 09:40:53.477070

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c9b7605de680'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    #op.drop_table('stats')
    #op.drop_table('materia')
    #op.drop_table('repair')
    #op.drop_table('weapon')
    op.create_table(
        'stats'
        ,sa.Column('id', sa.String, primary_key=True)
        ,sa.Column("str", sa.Integer)
        ,sa.Column("vit", sa.Integer)
        ,sa.Column("dex", sa.Integer)
        ,sa.Column('int', sa.Integer)
        ,sa.Column('mnd', sa.Integer)
        ,sa.Column('pie', sa.Integer)
        ,sa.Column('det', sa.Integer)
        ,sa.Column('spl', sa.Integer)
        ,sa.Column('skl', sa.Integer)
        ,sa.Column('dhr', sa.Integer)
        ,sa.Column('ten', sa.Integer)
    )
    op.create_table(
        'materia'
        ,sa.Column('id', sa.String, primary_key=True)
        ,sa.Column('slots', sa.Integer)
        ,sa.Column('melderJob', sa.String)
        ,sa.Column('melderLevel', sa.Integer)
        ,sa.Column('advancedMelding', sa.Boolean)
    )
    op.create_table(
        'repair'
        ,sa.Column('id', sa.String, primary_key=True)
        ,sa.Column('job', sa.String)
        ,sa.Column('level', sa.Integer)
        ,sa.Column('material', sa.String)
    )
    op.create_table(
        'weapon'
        ,sa.Column('id', sa.String, primary_key=True)
        ,sa.Column('url', sa.String)
        ,sa.Column('pictureUrl', sa.String)
        ,sa.Column('name',sa.String)
        ,sa.Column('rarity', sa.String)
        ,sa.Column('untradeable', sa.Boolean)
        ,sa.Column('unique', sa.Boolean)
        ,sa.Column('slot', sa.String)
        ,sa.Column('itemLevel', sa.Integer)
        ,sa.Column('jobs', sa.String)
        ,sa.Column('level', sa.Integer)
        ,sa.Column('companyCrest', sa.Boolean)
        ,sa.Column('armorie', sa.Boolean)
        ,sa.Column('glamourChest', sa.Boolean)
        ,sa.Column('dyeable', sa.Boolean)
        ,sa.Column('extractable', sa.Boolean)
        ,sa.Column('projectable', sa.Boolean)
        ,sa.Column('desynth', sa.Float)
        ,sa.Column('materia_id', sa.String, sa.ForeignKey('materia.id'))
        ,sa.Column('stats_id', sa.String, sa.ForeignKey('stats.id'))
        ,sa.Column('repair_id', sa.String, sa.ForeignKey('repair.id'))
    )
    pass


def downgrade():
    pass
