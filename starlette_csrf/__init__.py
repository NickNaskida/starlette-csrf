"""Starlette middleware implementing Double Submit Cookie technique to mitigate CSRF."""

__version__ = "0.0.0"

from starlette_csrf.middleware import CSRFMiddleware  # noqa: F401