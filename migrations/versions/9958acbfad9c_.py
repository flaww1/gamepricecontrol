"""empty message

Revision ID: 9958acbfad9c
Revises: 0522aa70700a
Create Date: 2020-06-03 15:42:31.163855

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9958acbfad9c'
down_revision = '0522aa70700a'
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
