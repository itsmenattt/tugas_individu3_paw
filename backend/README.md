# Product Review Analyzer

Pyramid + React app to analyze product reviews with Hugging Face sentiment and Gemini key-point extraction. Results are stored in PostgreSQL and exposed via a simple API.

## Prerequisites
- Python 3.13 (virtual env recommended)
- Node.js 18+
- PostgreSQL database
- API keys: `HUGGINGFACE_API_TOKEN` and `GEMINI_API_KEY`

## Environment variables
Set these before running the backend:
- `DATABASE_URL` – e.g. `postgresql+psycopg2://user:pass@localhost:5432/reviews`
- `HUGGINGFACE_API_TOKEN` – token for Hugging Face Inference API
- `HF_SENTIMENT_MODEL` (optional) – defaults to `distilbert-base-uncased-finetuned-sst-2-english`
- `GEMINI_API_KEY` – Google Generative AI key
- `GEMINI_MODEL` (optional) – defaults to `gemini-1.5-flash`

## Backend setup
```bash
# from backend/
python -m venv env
./env/Scripts/activate  # Windows PowerShell
pip install --upgrade pip setuptools
pip install -e ".[testing]"

# Apply migrations
alembic -c development.ini upgrade head

# Run dev server
pserve development.ini --reload
```

## Frontend setup
```bash
# from backend/frontend
npm install
npm run dev
# or build
npm run build
```
The frontend expects `VITE_API_BASE_URL` (default `http://localhost:6543`).

## API
- `POST /api/analyze-review` – body `{ "text": "..." }`, returns sentiment, score, key_points, saved id
- `GET /api/reviews` – returns `{ items: [...] }`
- `GET /api/health` – health check

## Testing
```bash
pytest
```
External services are monkeypatched in tests, so they run offline.

## Notes
- CORS is enabled for `GET/POST/OPTIONS` via a Pyramid tween.
- Alembic migration `20251214_0001_create_product_reviews.py` creates the `product_reviews` table.
