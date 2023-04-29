"""add posts, last_seen

Revision ID: 87264a166511
Revises: dbf238537092
Create Date: 2023-04-21 16:29:43.269255

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87264a166511'
down_revision = 'dbf238537092'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('content', sa.String(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], name='fk_posts_author_id', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('profiles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('last_seen', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('profiles', schema=None) as batch_op:
        batch_op.drop_column('last_seen')

    op.drop_table('posts')
    # ### end Alembic commands ###
