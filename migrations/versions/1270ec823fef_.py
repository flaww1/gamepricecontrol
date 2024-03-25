"""empty message

Revision ID: 1270ec823fef
Revises: fb4db2c12c03
Create Date: 2020-06-03 15:46:10.211591

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1270ec823fef'
down_revision = 'fb4db2c12c03'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('games', sa.Column('game_review', sa.String(length=120), nullable=True))
    op.create_index(op.f('ix_games_game_review'), 'games', ['game_review'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_games_game_review'), table_name='games')
    op.drop_column('games', 'game_review')
    # ### end Alembic commands ###