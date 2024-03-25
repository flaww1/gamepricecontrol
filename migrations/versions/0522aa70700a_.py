"""empty message

Revision ID: 0522aa70700a
Revises: 28099be21801
Create Date: 2020-06-03 15:07:15.302984

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0522aa70700a'
down_revision = '28099be21801'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('games', 'game_description',
               existing_type=mysql.VARCHAR(length=999),
               nullable=True)
    op.create_index(op.f('ix_games_game_video'), 'games', ['game_video'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_games_game_video'), table_name='games')
    op.alter_column('games', 'game_description',
               existing_type=mysql.VARCHAR(length=999),
               nullable=False)
    # ### end Alembic commands ###
