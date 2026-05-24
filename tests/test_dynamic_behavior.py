import pytest

from pages.base_page import BasePage
from pages.dashboard_page import DashboardPage
from tests.test_data.constants import CHECK_TYPE_HTTP


@pytest.mark.demoTest
class TestDynamicBehavior:

    def test_search_navigates_to_observability(self, page):
        """Filter by check type test."""

        dashboard = DashboardPage(page)
        base_page = BasePage(page)

        # Verifies dashboard is displayed before interacting with search
        dashboard.wait_for_dashboard()

        dashboard.click_check_type_dropdown()
        dashboard.page.get_by_role("option").filter(has_text=CHECK_TYPE_HTTP).first.click()

        # Verify the dashboard headings update to reflect the selected filter
        dashboard.wait_for_filtered_headings(CHECK_TYPE_HTTP)
        assert any(
             CHECK_TYPE_HTTP.lower() in heading.lower()
            for heading in dashboard.get_visible_dashboard_headings()
        ), f"Expected panel headers to include the selected {CHECK_TYPE_HTTP} option"