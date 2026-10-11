from semiconductor_ai_platform.config.settings import Settings


def test_settings_defaults_are_valid():
    settings = Settings(_env_file=None)
    assert settings.environment == "local"
    assert settings.api_v1_prefix == "/api/v1"
    assert settings.enable_request_id_middleware is True


def test_settings_accept_test_environment():
    settings = Settings(environment="test", _env_file=None)
    assert settings.environment == "test"
