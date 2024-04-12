"""create database

Revision ID: e1f91e6e2e2f
Revises: none
Create Date: 2024-04-05 20:39:48.954191

"""

import sqlalchemy as sa
from alembic import op

revision = "e1f91e6e2e2f"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "Cards",
        sa.Column("number", sa.Integer(), nullable=False),
        sa.Column("english_word", sa.Text(), nullable=True),
        sa.Column("english_sentence", sa.Text(), nullable=True),
        sa.Column("portuguese_word", sa.Text(), nullable=True),
        sa.Column("portuguese_sentence", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("number"),
    )
    op.create_table(
        "Piles",
        sa.Column("pile_name", sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint("pile_name"),
    )
    op.create_table(
        "State",
        sa.Column("index", sa.Integer(), nullable=False),
        sa.Column("card_order", sa.ARRAY(sa.Integer()), nullable=True),
        sa.Column("chosen_pile_name", sa.Text(), nullable=True),
        sa.ForeignKeyConstraint(
            ["chosen_pile_name"],
            ["Piles.pile_name"],
        ),
        sa.PrimaryKeyConstraint("index"),
    )


def downgrade():
    op.drop_table("State")
    op.drop_table("Piles")
    op.drop_table("Cards")
