"""empty message

Revision ID: 9784004b3235
Revises: 571978fb6cd5
Create Date: 2021-11-15 23:39:53.159277

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '9784004b3235'
down_revision = '571978fb6cd5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('equipment', 'pcss')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('equipment', sa.Column('pcss', mysql.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###