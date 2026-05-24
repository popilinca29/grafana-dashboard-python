import pytest

from pages.base_page import BasePage
from pages.dashboard_page import DashboardPage


@pytest.mark.demoTest
class TestSearchFilter:

    def test_search_navigates_to_observability(self, page):
        """Click the dashboard search, enter 'observability', and verify navigation."""

        dashboard = DashboardPage(page)
        base_page = BasePage(page)

        # Verifies dashboard is displayed before interacting with search
        dashboard.wait_for_dashboard()

        # Remember starting URL for back-navigation validation
        start_url = page.url
        dashboard.search_and_wait_for_heading("observability", heading_text="Observability", target_path="/observability")

        # Validate navigation occurred by checking URL
        assert "/observability" in page.url

        # Navigate back and verify we returned to the original dashboard URL
        page.go_back()
        base_page.validate_url(start_url)
