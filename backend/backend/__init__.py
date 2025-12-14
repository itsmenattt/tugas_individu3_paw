import os
from pathlib import Path

from dotenv import load_dotenv
from pyramid.config import Configurator


def main(global_config, **settings):
    """This function returns a Pyramid WSGI application."""

    # Load .env file if it exists
    env_path = Path(__file__).parent.parent / '.env'
    if env_path.exists():
        load_dotenv(env_path)

    # Allow DATABASE_URL env var to override the ini default for portability
    database_url = os.getenv("DATABASE_URL")
    if database_url:
        settings["sqlalchemy.url"] = database_url

    with Configurator(settings=settings) as config:
        config.include("pyramid_jinja2")
        config.include(".routes")
        config.include(".models")
        # Place CORS tween without explicit dependency to avoid ordering conflicts
        config.add_tween("backend.cors.cors_tween_factory")
        config.scan()
    return config.make_wsgi_app()
