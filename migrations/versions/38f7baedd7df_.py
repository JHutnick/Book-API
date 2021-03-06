"""empty message

Revision ID: 38f7baedd7df
Revises: fa3419a9b35f
Create Date: 2018-07-10 19:31:12.832844

"""

# revision identifiers, used by Alembic.
revision = '38f7baedd7df'
down_revision = 'fa3419a9b35f'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('notes',
    sa.Column('noteid', sa.Integer(), nullable=False),
    sa.Column('bookid', sa.Integer(), nullable=True),
    sa.Column('userid', sa.Integer(), nullable=True),
    sa.Column('text', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('noteid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('notes')
    # ### end Alembic commands ###
