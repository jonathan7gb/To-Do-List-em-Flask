"""empty message

Revision ID: b99b87ce667a
Revises: 
Create Date: 2025-07-24 15:36:49.164147

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b99b87ce667a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tarefa',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('titulo', sa.String(length=100), nullable=True),
    sa.Column('descricao', sa.String(length=100), nullable=True),
    sa.Column('status', sa.String(length=20), nullable=False),
    sa.Column('data_envio', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tarefa')
    # ### end Alembic commands ###
