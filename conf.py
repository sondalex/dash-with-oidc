import os


def validate_boolean_env_var(value: str) -> bool:
    if value.isdigit():
        return bool(int(value))
    if value.lower() == "false":
        return False
    if value.lower() == "true":
        return True
    raise EnvironmentError("Expected value to be positive")


def validate_integer_env_var(value: str) -> int:
    if not value.isdigit():
        raise EnvironmentError("Expected value to be parsable as integer")
    return int(value)


DEBUG = validate_boolean_env_var(os.environ.get("DASH_WITH_AUTH_DEBUG", "false"))

PORT = validate_integer_env_var(os.environ.get("DASH_WITH_AUTH_PORT", "8050"))


SECRET_KEY = os.environ["DASH_WITH_AUTH_SECRET"]


OIDC_ID = os.environ["DASH_WITH_AUTH_OIDC_ID"]


OIDC_SECRET = os.environ["DASH_WITH_AUTH_OIDC_SECRET"]


OIDC_METADATA_URL = os.environ["DASH_WITH_AUTH_OIDC_METADATA_URL"]

HOST = os.environ.get("DASH_WITH_AUTH_HOST", "127.0.0.1")

OIDC_FORCE_HTTPS = validate_boolean_env_var(os.environ.get("DASH_WITH_AUTH_OIDC_FORCE_HTTPS", "false"))
