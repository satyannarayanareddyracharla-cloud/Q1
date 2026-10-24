import logging

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

logger = logging.getLogger("selenium_tests")
logger.setLevel(logging.INFO)
if not logger.handlers:
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
    logger.addHandler(handler)


@pytest.fixture(scope="function")
def driver():
    """Create and close a browser instance for each test."""
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    try:
        logger.info("Starting Chrome WebDriver for a new test session.")
        browser = webdriver.Chrome(service=Service(), options=options)
    except Exception as exc:  # pragma: no cover - environment failure path
        logger.exception("Failed to start Chrome WebDriver.")
        pytest.exit(f"Unable to start Chrome: {exc}")

    yield browser

    try:
        browser.quit()
        logger.info("Closed Chrome WebDriver after test execution.")
    except Exception:  # pragma: no cover - cleanup protection
        logger.exception("Error while closing the browser during cleanup.")
