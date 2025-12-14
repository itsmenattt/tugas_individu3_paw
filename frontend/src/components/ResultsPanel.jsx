function ResultsPanel({ result, loading, error }) {
  if (loading) {
    return <div className="card muted">Analyzing your review...</div>;
  }

  if (error) {
    return <div className="card error">{error}</div>;
  }

  if (!result) {
    return <div className="card muted">Submit a review to see results.</div>;
  }

  return (
    <div className="card">
      <div className="card-header compact">
        <h3>Latest Analysis</h3>
        <span className={`pill pill-${result.sentiment_label}`}>
          {result.sentiment_label}
        </span>
      </div>
      <div className="grid two">
        <div>
          <p className="label">Product</p>
          <p className="value">{result.product_name || '—'}</p>
        </div>
        <div>
          <p className="label">Sentiment score</p>
          <p className="value">{result.sentiment_score.toFixed(3)}</p>
        </div>
        <div>
          <p className="label">Review text</p>
          <p className="value muted-text">{result.review_text}</p>
        </div>
      </div>
      <div className="keypoints">
        <p className="label">Key points</p>
        <ul>
          {(result.key_points || []).map((point, idx) => (
            <li key={`${point}-${idx}`}>{point}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default ResultsPanel;
