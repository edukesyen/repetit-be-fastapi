"""update user, add topic, remove item

Revision ID: 23a6a7beee68
Revises: 931b5ec4f961
Create Date: 2024-06-19 00:11:08.402345

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '23a6a7beee68'
down_revision: Union[str, None] = '931b5ec4f961'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # Drop the foreign key constraint on topics referencing students
    op.drop_constraint('topics_owner_id_fkey', 'topics', type_='foreignkey')
    
    # Drop indexes and tables
    op.drop_index('ix_students_email', table_name='students')
    op.drop_table('students')
    op.drop_index('ix_items_description', table_name='items')
    op.drop_index('ix_items_title', table_name='items')
    op.drop_table('items')
    
    # Modify topics table
    op.add_column('topics', sa.Column('name', sa.String(), nullable=True))
    op.add_column('topics', sa.Column('user_id', sa.Integer(), nullable=True))
    op.drop_index('ix_topics_description', table_name='topics')
    op.drop_index('ix_topics_title', table_name='topics')
    op.create_index(op.f('ix_topics_name'), 'topics', ['name'], unique=False)
    op.create_foreign_key(None, 'topics', 'users', ['user_id'], ['id'])
    op.drop_column('topics', 'owner_id')
    op.drop_column('topics', 'title')
    op.drop_column('topics', 'description')
    
    # Modify users table
    op.add_column('users', sa.Column('nickname', sa.String(), nullable=False))
    op.add_column('users', sa.Column('full_name', sa.String(), nullable=False))
    op.add_column('users', sa.Column('role', sa.Enum('STUDENT', 'MENTOR', name='userrole'), nullable=True))
    op.drop_column('users', 'is_human')
    # ### end Alembic commands ###

def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # Add back columns to users table
    op.add_column('users', sa.Column('is_human', sa.Boolean(), nullable=True))
    op.drop_column('users', 'role')
    op.drop_column('users', 'full_name')
    op.drop_column('users', 'nickname')
    
    # Add back columns to topics table
    op.add_column('topics', sa.Column('description', sa.String(), nullable=True))
    op.add_column('topics', sa.Column('title', sa.String(), nullable=True))
    op.add_column('topics', sa.Column('owner_id', sa.Integer(), nullable=True))
    op.drop_constraint(None, 'topics', type_='foreignkey')
    op.drop_index(op.f('ix_topics_name'), table_name='topics')
    op.create_index('ix_topics_title', 'topics', ['title'], unique=False)
    op.create_index('ix_topics_description', 'topics', ['description'], unique=False)
    op.drop_column('topics', 'user_id')
    op.drop_column('topics', 'name')
    
    # Recreate tables and indexes
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_items_title', 'items', ['title'], unique=False)
    op.create_index('ix_items_description', 'items', ['description'], unique=False)
    
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_students_email', 'students', ['email'], unique=False)
    
    # Recreate the foreign key constraint
    op.create_foreign_key('topics_owner_id_fkey', 'topics', 'students', ['owner_id'], ['id'])
    # ### end Alembic commands ###


# def upgrade() -> None:
#     # ### commands auto generated by Alembic - please adjust! ###
#     op.drop_index('ix_students_email', table_name='students')
#     op.drop_table('students')
#     op.drop_index('ix_items_description', table_name='items')
#     op.drop_index('ix_items_title', table_name='items')
#     op.drop_table('items')
#     op.add_column('topics', sa.Column('name', sa.String(), nullable=True))
#     op.add_column('topics', sa.Column('user_id', sa.Integer(), nullable=True))
#     op.drop_index('ix_topics_description', table_name='topics')
#     op.drop_index('ix_topics_title', table_name='topics')
#     op.create_index(op.f('ix_topics_name'), 'topics', ['name'], unique=False)
#     op.drop_constraint('topics_owner_id_fkey', 'topics', type_='foreignkey')
#     op.create_foreign_key(None, 'topics', 'users', ['user_id'], ['id'])
#     op.drop_column('topics', 'owner_id')
#     op.drop_column('topics', 'title')
#     op.drop_column('topics', 'description')
#     op.add_column('users', sa.Column('nickname', sa.String(), nullable=False))
#     op.add_column('users', sa.Column('full_name', sa.String(), nullable=False))
#     op.add_column('users', sa.Column('role', sa.Enum('STUDENT', 'MENTOR', name='userrole'), nullable=True))
#     op.drop_column('users', 'is_human')
#     # ### end Alembic commands ###


# def downgrade() -> None:
#     # ### commands auto generated by Alembic - please adjust! ###
#     op.add_column('users', sa.Column('is_human', sa.BOOLEAN(), autoincrement=False, nullable=True))
#     op.drop_column('users', 'role')
#     op.drop_column('users', 'full_name')
#     op.drop_column('users', 'nickname')
#     op.add_column('topics', sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True))
#     op.add_column('topics', sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True))
#     op.add_column('topics', sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=True))
#     op.drop_constraint(None, 'topics', type_='foreignkey')
#     op.create_foreign_key('topics_owner_id_fkey', 'topics', 'students', ['owner_id'], ['id'])
#     op.drop_index(op.f('ix_topics_name'), table_name='topics')
#     op.create_index('ix_topics_title', 'topics', ['title'], unique=False)
#     op.create_index('ix_topics_description', 'topics', ['description'], unique=False)
#     op.drop_column('topics', 'user_id')
#     op.drop_column('topics', 'name')
#     op.create_table('items',
#     sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
#     sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True),
#     sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
#     sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=True),
#     sa.ForeignKeyConstraint(['owner_id'], ['users.id'], name='items_owner_id_fkey'),
#     sa.PrimaryKeyConstraint('id', name='items_pkey')
#     )
#     op.create_index('ix_items_title', 'items', ['title'], unique=False)
#     op.create_index('ix_items_description', 'items', ['description'], unique=False)
#     op.create_table('students',
#     sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
#     sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
#     sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=True),
#     sa.Column('hashed_password', sa.VARCHAR(), autoincrement=False, nullable=True),
#     sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True),
#     sa.Column('role', postgresql.ENUM('ADMIN', 'STUDENT', 'MENTOR', name='userrole'), autoincrement=False, nullable=True),
#     sa.PrimaryKeyConstraint('id', name='students_pkey')
#     )
#     op.create_index('ix_students_email', 'students', ['email'], unique=True)
#     # ### end Alembic commands ###