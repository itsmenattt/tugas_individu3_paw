import { useState } from 'react';

function ReviewForm({ onSubmit, loading }) {
  const [product, setProduct] = useState('');
  const [text, setText] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    if (!product.trim() || !text.trim()) return;
    onSubmit({
      product: product.trim(),
      review: text.trim(),
    });
  };

  return (
    <form className="card" onSubmit={handleSubmit}>
      <div className="card-header">
        <h2>Product Review Analyzer</h2>
        <p>Paste a customer review to get instant sentiment and key points.</p>
      </div>
      <label className="field">
        <span className="label">Product name</span>
        <input
          type="text"
          className="input"
          placeholder="e.g., Wireless Headphones X10"
          value={product}
          onChange={(e) => setProduct(e.target.value)}
        />
      </label>
      <textarea
        className="input"
        placeholder="Type or paste a product review..."
        value={text}
        onChange={(e) => setText(e.target.value)}
        rows={6}
      />
      <div className="actions">
        <button type="submit" disabled={loading || !text.trim() || !product.trim()}>
          {loading ? 'Analyzing...' : 'Analyze Review'}
        </button>
        <span className="hint">Uses Hugging Face for sentiment and Gemini for key points.</span>
      </div>
    </form>
  );
}

export default ReviewForm;
