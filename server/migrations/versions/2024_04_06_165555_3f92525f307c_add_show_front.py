"""show front

Revision ID: 3f92525f307c
Revises: f47a16df0e17
Create Date: 2024-04-06 16:55:55.220759

"""

from alembic import op
import sqlalchemy as sa


revision = "3f92525f307c"
down_revision = "f47a16df0e17"
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table("State", schema=None) as batch_op:
        batch_op.add_column(sa.Column("show_front", sa.Boolean(), nullable=True))


def downgrade():
    with op.batch_alter_table("State", schema=None) as batch_op:
        batch_op.drop_column("show_front")
