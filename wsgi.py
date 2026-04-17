"""WSGI entry point for production servers."""

from main import app


# Expose `application` for generic WSGI hosts
application = app
