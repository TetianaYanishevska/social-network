"""add profiles table

Revision ID: 9707ffb950c4
Revises: 00f628824eaa
Create Date: 2023-04-17 02:17:13.736380

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9707ffb950c4'
down_revision = '00f628824eaa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profiles',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('about_me', sa.String(length=300), nullable=True),
    sa.Column('linkedin', sa.String(length=50), nullable=True),
    sa.Column('facebook', sa.String(length=50), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='fk_profiles_user_id'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profiles')
    # ### end Alembic commands ###