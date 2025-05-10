# tests/test_settings.py

import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))

from settings import Settings


def test_settings_loaded():
    settings = Settings()
    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "mlops-test"
    assert settings.FAKE_API_KEY == "test-key-123"
