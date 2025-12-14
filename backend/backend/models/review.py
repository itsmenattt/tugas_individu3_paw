import datetime as dt
from typing import Any

from sqlalchemy import Column, DateTime, Float, Integer, String, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func
from sqlalchemy.types import JSON

from .meta import Base


class ProductReview(Base):
    __tablename__ = "product_reviews"

    id = Column(Integer, primary_key=True)
    product_name = Column(String(255), nullable=True)
    review_text = Column(Text, nullable=False)
    sentiment_label = Column(String(32), nullable=False)
    sentiment_score = Column(Float, nullable=False)
    key_points = Column(JSON().with_variant(JSONB, "postgresql"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    def to_dict(self) -> dict[str, Any]:
        return {
            "id": self.id,
            "product_name": self.product_name,
            "review_text": self.review_text,
            "sentiment_label": self.sentiment_label,
            "sentiment_score": self.sentiment_score,
            "key_points": self.key_points or [],
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }
