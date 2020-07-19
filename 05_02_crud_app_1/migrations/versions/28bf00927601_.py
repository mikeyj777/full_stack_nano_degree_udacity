"""empty message

Revision ID: 28bf00927601
Revises: 021ca68f416b
Create Date: 2020-07-19 12:46:41.149685

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '28bf00927601'
down_revision = '021ca68f416b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('completed', sa.Boolean(), nullable=True))

    op.execute('UPDATE todos SET completed = False WHERE completed is NULL;')

    op.update_column('todos', 'completed', nullable = False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todos', 'completed')
    # ### end Alembic commands ###
