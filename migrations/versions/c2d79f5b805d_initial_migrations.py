"""initial migrations

Revision ID: c2d79f5b805d
Revises: 
Create Date: 2019-05-03 12:12:07.300331

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2d79f5b805d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admins',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('first_name', sa.String(length=100), nullable=True),
    sa.Column('last_name', sa.String(length=100), nullable=True),
    sa.Column('username', sa.String(length=72), nullable=True),
    sa.Column('password_hash', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_admins_email'), 'admins', ['email'], unique=True)
    op.create_index(op.f('ix_admins_username'), 'admins', ['username'], unique=True)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('device_id', sa.Text(), nullable=False),
    sa.Column('event_code', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_timestamp'), 'users', ['timestamp'], unique=False)
    op.create_table('events',
    sa.Column('admins', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('body', sa.Text(), nullable=False),
    sa.Column('event_date', sa.DateTime(), nullable=False),
    sa.Column('event_id', sa.String(length=8), nullable=False),
    sa.ForeignKeyConstraint(['admins'], ['admins.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_events_event_date'), 'events', ['event_date'], unique=False)
    op.create_table('questions',
    sa.Column('event', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=120), nullable=False),
    sa.ForeignKeyConstraint(['event'], ['events.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('responses',
    sa.Column('questions', sa.Integer(), nullable=True),
    sa.Column('respondent', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('body', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['questions'], ['questions.id'], ),
    sa.ForeignKeyConstraint(['respondent'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_responses_timestamp'), 'responses', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_responses_timestamp'), table_name='responses')
    op.drop_table('responses')
    op.drop_table('questions')
    op.drop_index(op.f('ix_events_event_date'), table_name='events')
    op.drop_table('events')
    op.drop_index(op.f('ix_users_timestamp'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_admins_username'), table_name='admins')
    op.drop_index(op.f('ix_admins_email'), table_name='admins')
    op.drop_table('admins')
    # ### end Alembic commands ###
