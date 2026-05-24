import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

# Load environment variables from .env file (local runs)
load_dotenv()

# Configuration (works for local + CI)
BASE_URL = os.getenv("BASE_URL")

BROWSER = os.getenv("BROWSER", "chromium")
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "30000"))


@pytest.fixture
def page():
    with sync_playwright() as p:

        # Select browser dynamically
        if BROWSER == "firefox":
            browser_type = p.firefox
        elif BROWSER == "webkit":
            browser_type = p.webkit
        else:
            browser_type = p.chromium

        # Launch browser
        browser = browser_type.launch(headless=HEADLESS)

        # Create isolated session
        context = browser.new_context()
        context.set_default_timeout(DEFAULT_TIMEOUT)

        page = context.new_page()

        # Navigate to application
        page.goto(BASE_URL)

        yield page

        # Cleanup
        context.close()
        browser.close()