"""Add ResetToken table

Revision ID: a4629e82072d
Revises: 
Create Date: 2025-05-29 17:21:36.458944

"""
from alembic import op
import sqlalchemy as sa



# revision identifiers, used by Alembic.
revision = 'a4629e82072d'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reset_tokens',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('token', sa.String(), nullable=False),
    sa.Column('expires_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_reset_tokens_email'), 'reset_tokens', ['email'], unique=False)
    op.create_index(op.f('ix_reset_tokens_id'), 'reset_tokens', ['id'], unique=False)
    op.create_index(op.f('ix_reset_tokens_token'), 'reset_tokens', ['token'], unique=True)
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_reset_tokens_token'), table_name='reset_tokens')
    op.drop_index(op.f('ix_reset_tokens_id'), table_name='reset_tokens')
    op.drop_index(op.f('ix_reset_tokens_email'), table_name='reset_tokens')
    op.drop_table('reset_tokens')
    # ### end Alembic commands ###
