def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('health', '/api/health')
    config.add_route('analyze_review', '/api/analyze-review')
    config.add_route('list_reviews', '/api/reviews')
