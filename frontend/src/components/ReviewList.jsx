function formatDate(value) {
  if (!value) return '—';
  return new Date(value).toLocaleString();
}

function ReviewList({ items }) {
  if (!items.length) {
    return <div className="card muted">No reviews analyzed yet.</div>;
  }

  return (
    <div className="card">
      <div className="card-header compact">
        <h3>Recent Reviews</h3>
        <span className="label">{items.length} saved</span>
      </div>
      <ul className="review-list">
        {items.map((item) => (
          <li key={item.id} className="review-row">
            <div className="review-meta">
              <span className={`pill pill-${item.sentiment_label}`}>{item.sentiment_label}</span>
              <span className="timestamp">{formatDate(item.created_at)}</span>
            </div>
            {item.product_name ? (
              <p className="label">Product: {item.product_name}</p>
            ) : null}
            <p className="review-text">{item.review_text}</p>
            <div className="keypoints-inline">
              {(item.key_points || []).map((point, idx) => (
                <span key={`${item.id}-${idx}`} className="chip">{point}</span>
              ))}
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ReviewList;
