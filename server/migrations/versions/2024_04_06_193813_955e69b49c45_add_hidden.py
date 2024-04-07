"""add hidden

Revision ID: 955e69b49c45
Revises: 3f92525f307c
Create Date: 2024-04-06 19:38:13.968694

"""

from alembic import op
import sqlalchemy as sa


revision = "955e69b49c45"
down_revision = "3f92525f307c"
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table("Cards", schema=None) as batch_op:
        batch_op.add_column(sa.Column("hidden", sa.Boolean(), nullable=True))


def downgrade():
    with op.batch_alter_table("Cards", schema=None) as batch_op:
        batch_op.drop_column("hidden")
