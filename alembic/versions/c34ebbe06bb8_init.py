"""init

Revision ID: c34ebbe06bb8
Revises: 
Create Date: 2024-06-29 12:03:35.820664

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c34ebbe06bb8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=16), nullable=False),
    sa.Column('title', sa.String(length=256), nullable=False),
    sa.Column('author', sa.String(length=256), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_book')),
    sa.UniqueConstraint('code', name=op.f('uq_book_code'))
    )
    op.create_index(op.f('ix_book_id'), 'book', ['id'], unique=False)
    op.create_table('member',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=16), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('penalized_until', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_member')),
    sa.UniqueConstraint('code', name=op.f('uq_member_code'))
    )
    op.create_index(op.f('ix_member_id'), 'member', ['id'], unique=False)
    op.create_table('borrow',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=True),
    sa.Column('member_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('is_returned', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], name=op.f('fk_borrow_book_id_book')),
    sa.ForeignKeyConstraint(['member_id'], ['member.id'], name=op.f('fk_borrow_member_id_member')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_borrow'))
    )
    op.create_index(op.f('ix_borrow_book_id'), 'borrow', ['book_id'], unique=False)
    op.create_index(op.f('ix_borrow_id'), 'borrow', ['id'], unique=False)
    op.create_index(op.f('ix_borrow_member_id'), 'borrow', ['member_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_borrow_member_id'), table_name='borrow')
    op.drop_index(op.f('ix_borrow_id'), table_name='borrow')
    op.drop_index(op.f('ix_borrow_book_id'), table_name='borrow')
    op.drop_table('borrow')
    op.drop_index(op.f('ix_member_id'), table_name='member')
    op.drop_table('member')
    op.drop_index(op.f('ix_book_id'), table_name='book')
    op.drop_table('book')
    # ### end Alembic commands ###
