import logging

from selenium.webdriver.common.by import By

from pages.base_page import BasePage

logger = logging.getLogger("selenium_tests")


class LoginPage(BasePage):
    """Page object encapsulating the login page behavior."""

    URL_PATH = "/login"
    SUCCESS_MESSAGE = "You logged into a secure area!"
    INVALID_PASSWORD_MESSAGE = "Your password is invalid!"

    # Keep locators centralized in one place for maintainability.
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH_MESSAGE = (By.ID, "flash")

    def open(self) -> None:
        logger.info("Opening login page on %s", self.base_url)
        super().open(self.URL_PATH)

    def login(self, username: str, password: str) -> None:
        """Reusable login action for valid or invalid credentials."""
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        logger.info("Submitted login form for user '%s'.", username)

    @property
    def flash_message(self) -> str:
        message = self.find_element(self.FLASH_MESSAGE)
        logger.info("Read flash message: %s", message.text)
        return message.text

    def is_success_message_displayed(
        self, expected_text: str = SUCCESS_MESSAGE
    ) -> bool:
        is_displayed = expected_text in self.flash_message
        logger.info("Success message assertion: %s", is_displayed)
        return is_displayed
