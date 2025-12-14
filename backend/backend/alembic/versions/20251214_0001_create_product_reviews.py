"""create product_reviews table

Revision ID: 20251214_0001
Revises: 
Create Date: 2025-12-14 00:00:00
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "20251214_0001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "product_reviews",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("review_text", sa.Text(), nullable=False),
        sa.Column("sentiment_label", sa.String(length=32), nullable=False),
        sa.Column("sentiment_score", sa.Float(), nullable=False),
        sa.Column("key_points", sa.JSON(), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("CURRENT_TIMESTAMP"),
            nullable=False,
        ),
    )


def downgrade():
    op.drop_table("product_reviews")
