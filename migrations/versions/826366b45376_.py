"""empty message

Revision ID: 826366b45376
Revises: 
Create Date: 2020-04-28 11:57:23.395810

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '826366b45376'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todos')
    op.drop_table('todolists')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todolists',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('todolists_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='todolists_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('todos',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('completed', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('list_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['list_id'], ['todolists.id'], name='todos_list_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='todos_pkey')
    )
    # ### end Alembic commands ###