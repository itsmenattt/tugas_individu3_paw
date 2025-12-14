from backend.services.sentiment import SentimentResult
from backend.views import default


def test_analyze_and_list_reviews(testapp, monkeypatch):
    monkeypatch.setattr(
        default,
        "analyze_sentiment",
        lambda text: SentimentResult(label="positive", score=0.88),
    )
    monkeypatch.setattr(default, "extract_key_points", lambda text: ["fast", "compact"])

    res = testapp.post_json("/api/analyze-review", {"text": "Great device"}, status=200)

    assert res.json["sentiment_label"] == "positive"
    assert res.json["key_points"] == ["fast", "compact"]

    list_res = testapp.get("/api/reviews", status=200)
    assert len(list_res.json["items"]) >= 1


def test_notfound(testapp):
    res = testapp.get('/badurl', status=404)
    assert res.status_code == 404
