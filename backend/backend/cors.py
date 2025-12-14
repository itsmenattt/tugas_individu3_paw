from pyramid.response import Response


def cors_tween_factory(handler, registry):
    def cors_tween(request):
        # Preflight handling for simple API routes
        if request.method == "OPTIONS":
            response = Response()
            _apply_cors_headers(response)
            return response

        response = handler(request)
        _apply_cors_headers(response)
        return response

    return cors_tween


def _apply_cors_headers(response):
    response.headers.update(
        {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
            "Access-Control-Allow-Headers": "Content-Type,Authorization",
        }
    )
