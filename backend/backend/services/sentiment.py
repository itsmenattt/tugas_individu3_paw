import os
from dataclasses import dataclass
from typing import Optional

from huggingface_hub import InferenceClient


@dataclass
class SentimentResult:
    label: str
    score: float


def analyze_sentiment(text: str) -> SentimentResult:
    token = os.getenv("HUGGINGFACE_API_TOKEN")
    if not token:
        raise RuntimeError("HUGGINGFACE_API_TOKEN is not set")

    # Use a model that supports serverless inference API
    model_id = os.getenv(
        "HF_SENTIMENT_MODEL", "cardiffnlp/twitter-roberta-base-sentiment-latest"
    )

    client = InferenceClient(model=model_id, token=token)
    result = client.text_classification(text)

    if not result:
        raise RuntimeError("No sentiment prediction returned")

    top = result[0]
    label = (top.get("label") or "").lower()
    score: Optional[float] = top.get("score")

    if score is None:
        raise RuntimeError("Sentiment score missing")

    return SentimentResult(label=label, score=float(score))
