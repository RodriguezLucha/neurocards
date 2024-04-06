"""add pile name to card

Revision ID: f47a16df0e17
Revises: e1f91e6e2e2f
Create Date: 2024-04-06 11:14:29.845363

"""

from alembic import op
import sqlalchemy as sa


revision = "f47a16df0e17"
down_revision = "e1f91e6e2e2f"
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table("Cards", schema=None) as batch_op:
        batch_op.add_column(sa.Column("pile_name", sa.Text(), nullable=True))
        batch_op.create_foreign_key(None, "Piles", ["pile_name"], ["pile_name"])


def downgrade():
    with op.batch_alter_table("Cards", schema=None) as batch_op:
        batch_op.drop_constraint(None, type_="foreignkey")
        batch_op.drop_column("pile_name")
