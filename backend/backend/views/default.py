import logging
from typing import Any

from pyramid.httpexceptions import HTTPBadRequest, HTTPInternalServerError
from pyramid.view import view_config
from sqlalchemy.exc import SQLAlchemyError

from ..models import ProductReview
from ..services.keypoints import extract_key_points
from ..services.sentiment import analyze_sentiment

log = logging.getLogger(__name__)


@view_config(route_name="health", request_method="GET", renderer="json")
def health_check(request):
    return {"status": "ok"}


@view_config(route_name="analyze_review", request_method="POST", renderer="json")
def analyze_review(request):
    try:
        payload: dict[str, Any] = request.json_body or {}
    except ValueError:
        raise HTTPBadRequest(json_body={"error": "invalid JSON body"})
    raw_text = payload.get("text") or payload.get("review") or ""
    product_name = (payload.get("product_name") or payload.get("product") or "").strip()
    review_text = (raw_text or "").strip()

    if not review_text:
        raise HTTPBadRequest(json_body={"error": "review text is required"})

    try:
        sentiment = analyze_sentiment(review_text)
        key_points = extract_key_points(review_text)

        review = ProductReview(
            product_name=product_name or None,
            review_text=review_text,
            sentiment_label=sentiment.label,
            sentiment_score=sentiment.score,
            key_points=key_points,
        )
        request.dbsession.add(review)
        request.dbsession.flush()  # ensure id is available

        return {
            "id": review.id,
            "product_name": review.product_name,
            "sentiment_label": review.sentiment_label,
            "sentiment_score": review.sentiment_score,
            "key_points": review.key_points,
            "review_text": review.review_text,
            "created_at": review.created_at.isoformat() if review.created_at else None,
        }
    except HTTPBadRequest:
        raise
    except (SQLAlchemyError, Exception) as exc:  # noqa: BLE001
        log.exception("Failed to analyze review")
        raise HTTPInternalServerError(json_body={"error": "unable to analyze review"}) from exc


@view_config(route_name="list_reviews", request_method="GET", renderer="json")
def list_reviews(request):
    try:
        reviews = (
            request.dbsession.query(ProductReview)
            .order_by(ProductReview.created_at.desc())
            .all()
        )
        return {"items": [review.to_dict() for review in reviews]}
    except SQLAlchemyError as exc:
        log.exception("Failed to fetch reviews")
        raise HTTPInternalServerError(json_body={"error": "unable to fetch reviews"}) from exc
