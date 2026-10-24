from config.settings import BASE_URL, INVALID_PASSWORD, VALID_PASSWORD, VALID_USERNAME
from pages.login_page import LoginPage


def test_user_can_log_in_with_valid_credentials(driver):
    """Verify the login page accepts valid credentials and displays the success message."""
    login_page = LoginPage(driver, BASE_URL)
    login_page.open()

    login_page.login(VALID_USERNAME, VALID_PASSWORD)

    assert login_page.is_success_message_displayed()


def test_user_cannot_log_in_with_invalid_credentials(driver):
    """Verify the login page rejects invalid credentials with the expected validation message."""
    login_page = LoginPage(driver, BASE_URL)
    login_page.open()

    login_page.login(VALID_USERNAME, INVALID_PASSWORD)

    assert "Your password is invalid!" in login_page.flash_message
