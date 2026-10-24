# Selenium Login Automation

This project demonstrates a clean, maintainable Selenium test automation suite built with `pytest` and the page-object model.

## Project structure

- `config/` — environment and test configuration
- `pages/` — page objects for browser interactions
- `tests/` — automated test cases
- `conftest.py` — browser fixture and shared setup
- `pytest.ini` — pytest configuration
- `reports/` — generated HTML test report

## Setup

1. Create a virtual environment and activate it.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the tests:

   ```bash
   python -m pytest -q
   ```

The run generates a self-contained HTML report at `reports/report.html`.

## Test configuration

You can override the default target URL and credentials using environment variables:

PowerShell:

```powershell
$env:BASE_URL = "https://the-internet.herokuapp.com"
$env:VALID_USERNAME = "tomsmith"
$env:VALID_PASSWORD = "SuperSecretPassword!"
$env:INVALID_PASSWORD = "wrong-password"
```

Bash:

```bash
export BASE_URL="https://the-internet.herokuapp.com"
export VALID_USERNAME="tomsmith"
export VALID_PASSWORD="SuperSecretPassword!"
export INVALID_PASSWORD="wrong-password"
```

## Notes

The suite uses Chrome in headless mode for stable CI execution.
