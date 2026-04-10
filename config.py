import os

SECRET_KEY = "super_secret_key_session"

FERNET_KEY = os.environ.get(
    "FERNET_KEY",
    b'yNRdWQt-y5OdWkK24NpG5n_EyHebu61mXi3LMR7Ua8g='
)