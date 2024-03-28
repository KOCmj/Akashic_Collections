"""empty message

Revision ID: 7559784a5578
Revises: 
Create Date: 2024-03-27 21:22:45.499916

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7559784a5578'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('IBSN', sa.String(length=150), nullable=True),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('author', sa.String(length=255), nullable=True),
    sa.Column('published_date', sa.String(length=25), nullable=True),
    sa.Column('category', sa.String(length=200), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book')
    # ### end Alembic commands ###
