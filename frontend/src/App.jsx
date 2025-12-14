import { useEffect, useState } from 'react';
import { analyzeReview, fetchReviews } from './api';
import ReviewForm from './components/ReviewForm';
import ResultsPanel from './components/ResultsPanel';
import ReviewList from './components/ReviewList';

function App() {
  const [latest, setLatest] = useState(null);
  const [reviews, setReviews] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const loadReviews = async () => {
    try {
      const data = await fetchReviews();
      setReviews(data.items || []);
    } catch (err) {
      setError(err.message);
    }
  };

  useEffect(() => {
    loadReviews();
  }, []);

  const handleSubmit = async ({ product, review }) => {
    setLoading(true);
    setError(null);
    try {
      const result = await analyzeReview(review, product);
      setLatest({ ...result, product_name: product });
      await loadReviews();
    } catch (err) {
      setError(err.message || 'Something went wrong');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page">
      <header className="page-header">
        <h1>Product Review Analyzer</h1>
        <p>Fast sentiment and key-point extraction for customer feedback.</p>
      </header>

      <main className="layout">
        <section className="column">
          <ReviewForm onSubmit={handleSubmit} loading={loading} />
          <ResultsPanel result={latest} loading={loading} error={error} />
        </section>
        <section className="column">
          <ReviewList items={reviews} />
        </section>
      </main>
    </div>
  );
}

export default App;
