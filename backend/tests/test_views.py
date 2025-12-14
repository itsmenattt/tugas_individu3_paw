from backend.models import ProductReview
from backend.services.sentiment import SentimentResult
from backend.views import default
from backend.views.notfound import notfound_view


def test_analyze_review_success(app_request, monkeypatch):
    monkeypatch.setattr(
        default,
        "analyze_sentiment",
        lambda text: SentimentResult(label="positive", score=0.92),
    )
    monkeypatch.setattr(default, "extract_key_points", lambda text: ["great battery", "light"])

    app_request.json_body = {"text": "I love this product"}

    result = default.analyze_review(app_request)

    assert result["sentiment_label"] == "positive"
    assert result["sentiment_score"] > 0
    assert len(result["key_points"]) == 2


def test_list_reviews_returns_saved_items(app_request, dbsession):
    review = ProductReview(
        review_text="Solid build",
        sentiment_label="neutral",
        sentiment_score=0.5,
        key_points=["solid", "durable"],
    )
    dbsession.add(review)
    dbsession.flush()

    response = default.list_reviews(app_request)

    assert len(response["items"]) == 1
    assert response["items"][0]["review_text"] == "Solid build"


def test_notfound_view(app_request):
    info = notfound_view(app_request)
    assert app_request.response.status_int == 404
    assert info == {}
