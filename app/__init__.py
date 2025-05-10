from app.api import app as app  # Explicit re-export

__all__ = ["app"]  # Inform Ruff and linters that 'app' is used intentionally
