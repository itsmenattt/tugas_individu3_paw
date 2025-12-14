import os
from typing import List

import google.generativeai as genai


def _configure_client() -> genai.GenerativeModel:
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is not set")

    genai.configure(api_key=api_key)
    model_id = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")
    return genai.GenerativeModel(model_id)


def extract_key_points(review_text: str) -> List[str]:
    model = _configure_client()

    prompt = (
        "Summarize the following product review into 3-5 concise bullet points. "
        "Return only the bullet points as plain text, one per line, no numbering.\n\n"
        f"Review:\n{review_text}"
    )

    response = model.generate_content(prompt)
    text = (response.text or "").strip()
    if not text:
        return []

    lines = [line.strip("-* •\t ") for line in text.splitlines() if line.strip()]
    return [line for line in lines if line][:5]
