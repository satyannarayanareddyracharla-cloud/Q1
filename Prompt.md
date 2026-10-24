# Selenium Test Automation Prompt

## Objective
Build and maintain a robust, enterprise-style Selenium test automation suite using Python, pytest, and the Page Object Model (POM). The suite should be readable, reusable, scalable, and easy to extend for future test scenarios.

## Mandatory Requirements
The implementation must include the following:

1. POM Model
   - Separate page behavior from test logic.
   - Encapsulate UI interactions in page classes.
   - Keep test cases focused on business verification rather than Selenium API details.
   - Files involved:
     - `pages/base_page.py`
     - `pages/login_page.py`
     - `tests/test_login.py`

2. Locator in one place
   - Store all UI locators in the page object classes.
   - Avoid scattered selectors across individual tests.
   - Centralize WebElement identifiers for easier maintenance.
   - Files involved:
     - `pages/login_page.py`
     - `pages/base_page.py`

3. Reusable login method
   - Create a single method like `login(username, password)` in the login page object.
   - Reuse it across valid and invalid login scenarios.
   - Files involved:
     - `pages/login_page.py`
     - `tests/test_login.py`

4. Code Smell Reduction
   - Avoid duplicated browser actions.
   - Minimize hard-coded element interactions inside test methods.
   - Use shared reusable helper methods.
   - Files involved:
     - `pages/base_page.py`
     - `conftest.py`
     - `tests/test_login.py`

5. Readability
   - Use clear class and method names.
   - Write concise, descriptive test names.
   - Keep the code structure clean and maintainable.
   - Files involved:
     - `pages/base_page.py`
     - `pages/login_page.py`
     - `tests/test_login.py`
     - `README.md`

6. Logging
   - Add logging for browser startup, navigation, user actions, and key validation results.
   - Log important events to support debugging and reporting.
   - Files involved:
     - `conftest.py`
     - `pages/base_page.py`
     - `pages/login_page.py`

7. HTML Reporting
   - Generate automation test reports in HTML format.
   - Ensure report output is easily readable for execution summaries.
   - Files involved:
     - `pytest.ini`
     - `reports/report.html`

## Project Structure

- `conftest.py` — shared pytest fixture for browser setup and teardown
- `config/settings.py` — environment-based configuration values
- `pages/base_page.py` — reusable page actions and waiting utilities
- `pages/login_page.py` — login page object with locators and login flow
- `tests/test_login.py` — automated login test scenarios
- `pytest.ini` — pytest configuration and HTML report generation
- `requirements.txt` — project dependencies
- `reports/report.html` — generated HTML test report
- `README.md` — project setup and usage guide

## Functional Scope

The automation suite validates the login flow of the Heroku app at:
https://the-internet.herokuapp.com

Covered scenarios:
- Successful login with valid credentials
- Failed login with invalid password

## Test Execution

Run the full suite:

```bash
python -m pytest -q
```

The project is configured to produce an HTML report automatically:

```bash
reports/report.html
```

## Tech Stack

- Python
- pytest
- Selenium WebDriver
- pytest-html
- Page Object Model (POM)

## Best Practices to Follow

- Keep test logic separate from page logic.
- Use waits instead of hard sleeps.
- Use centralized config for environment variables.
- Prefer descriptive names and clean structure.
- Ensure each test is independent and isolated.
- Capture logs and reports for debugging and validation.

## Example Design Pattern

```python
class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH_MESSAGE = (By.ID, "flash")

    def login(self, username, password):
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
```

## Outcome
The final test suite should be clean, maintainable, scalable, and compliant with enterprise-quality Selenium automation standards.
