"""Added application and contribution models

Revision ID: fd3a8b46b8cb
Revises: 4c1cf295618d
Create Date: 2024-09-29 20:53:19.200165

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd3a8b46b8cb'
down_revision = '4c1cf295618d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('application',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('reason', sa.String(length=255), nullable=False),
    sa.Column('date_submitted', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contribution',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sponsor_id', sa.Integer(), nullable=False),
    sa.Column('application_id', sa.Integer(), nullable=False),
    sa.Column('amount', sa.Float(), nullable=False),
    sa.Column('date_contributed', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['application_id'], ['application.id'], ),
    sa.ForeignKeyConstraint(['sponsor_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contribution')
    op.drop_table('application')
    # ### end Alembic commands ###
