"""add product_name to product_reviews

Revision ID: 20251214_0002
Revises: 20251214_0001
Create Date: 2025-12-14
"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "20251214_0002"
down_revision = "20251214_0001"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "product_reviews",
        sa.Column("product_name", sa.String(length=255), nullable=True),
    )


def downgrade() -> None:
    op.drop_column("product_reviews", "product_name")
