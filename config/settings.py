import os

BASE_URL = os.getenv("BASE_URL", "https://the-internet.herokuapp.com")
VALID_USERNAME = os.getenv("VALID_USERNAME", "tomsmith")
VALID_PASSWORD = os.getenv("VALID_PASSWORD", "SuperSecretPassword!")
INVALID_PASSWORD = os.getenv("INVALID_PASSWORD", "wrong-password")
