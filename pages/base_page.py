class BasePage:
    def __init__(self, page):
        self.page = page

    def goto(self, url):
        self.page.goto(url)

    def click(self, locator):
        self.page.locator(locator).click()

    def fill(self, locator, value):
        self.page.locator(locator).fill(value)

    def text(self, locator):
        return self.page.locator(locator).inner_text()

    def validate_url(self, expected_url: str, timeout: int = 30000) -> None:
        self.page.wait_for_url(expected_url, timeout=timeout)
        assert self.page.url == expected_url, (
            f"Expected URL after back navigation to be '{expected_url}', got '{self.page.url}'"
        )

    def is_visible(self, locator):
        return self.page.locator(locator).is_visible()