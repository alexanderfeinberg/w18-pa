"""migrate

Revision ID: 63ab990a4436
Revises: 
Create Date: 2022-11-04 11:00:51.511109

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '63ab990a4436'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('simple_person',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('bio', sa.String(length=2000), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('simple_person')
    # ### end Alembic commands ###
