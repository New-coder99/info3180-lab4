"""empty message

Revision ID: 073fd12243bb
Revises: f0c8ff3f5528
Create Date: 2024-03-06 19:13:33.168160

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '073fd12243bb'
down_revision = 'f0c8ff3f5528'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_profiles', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.String(length=128), nullable=True))
        batch_op.alter_column('last_name',
               existing_type=sa.VARCHAR(length=128),
               type_=sa.String(length=80),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_profiles', schema=None) as batch_op:
        batch_op.alter_column('last_name',
               existing_type=sa.String(length=80),
               type_=sa.VARCHAR(length=128),
               existing_nullable=True)
        batch_op.drop_column('password')

    # ### end Alembic commands ###
