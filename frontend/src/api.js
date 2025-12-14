const API_BASE = import.meta.env.VITE_API_BASE_URL || 'http://localhost:6543';

async function handleResponse(res) {
  const data = await res.json().catch(() => ({}));
  if (!res.ok) {
    const message = data.error || 'Request failed';
    throw new Error(message);
  }
  return data;
}

export async function analyzeReview(text, productName) {
  const res = await fetch(`${API_BASE}/api/analyze-review`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text, product_name: productName }),
  });
  return handleResponse(res);
}

export async function fetchReviews() {
  const res = await fetch(`${API_BASE}/api/reviews`);
  return handleResponse(res);
}
