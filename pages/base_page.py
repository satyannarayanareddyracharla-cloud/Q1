from __future__ import annotations

import logging
from typing import Tuple

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

logger = logging.getLogger("selenium_tests")


class BasePage:
    """Shared browser actions and waiting utilities."""

    DEFAULT_TIMEOUT = 10

    def __init__(self, driver: WebDriver, base_url: str):
        self.driver = driver
        self.base_url = base_url.rstrip("/")
        self.logger = logger

    def open(self, path: str = "") -> None:
        url = f"{self.base_url}/{path.lstrip('/')}" if path else self.base_url
        self.logger.info("Opening page: %s", url)
        self.driver.get(url)

    def wait_for_visible(self, locator: Tuple[str, str], timeout: int = DEFAULT_TIMEOUT):
        self.logger.debug("Waiting for element to be visible: %s", locator)
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_clickable(self, locator: Tuple[str, str], timeout: int = DEFAULT_TIMEOUT):
        self.logger.debug("Waiting for element to be clickable: %s", locator)
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def find_element(self, locator: Tuple[str, str], timeout: int = DEFAULT_TIMEOUT):
        self.logger.debug("Finding element: %s", locator)
        return self.wait_for_visible(locator, timeout)

    def type_text(self, locator: Tuple[str, str], value: str, timeout: int = DEFAULT_TIMEOUT) -> None:
        element = self.find_element(locator, timeout)
        self.logger.info("Typing into %s", locator)
        element.clear()
        element.send_keys(value)

    def click(self, locator: Tuple[str, str], timeout: int = DEFAULT_TIMEOUT) -> None:
        element = self.wait_for_clickable(locator, timeout)
        self.logger.info("Clicking element: %s", locator)
        element.click()
