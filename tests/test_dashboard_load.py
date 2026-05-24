import pytest

from pages.dashboard_page import DashboardPage


@pytest.mark.demoTest
class TestDashboard:

    def test_dashboard_loads_and_is_interactive(self, page):
        """Verify the dashboard loads and key UI components are interactive."""

        dashboard = DashboardPage(page)

        # Wait for the dashboard root view to render
        dashboard.wait_for_dashboard()

        # Verify core dashboard elements are visible
        assert dashboard.is_search_visible()
        assert dashboard.are_dashboard_headings_visible()
        assert dashboard.are_filters_visible()
        assert dashboard.is_create_new_check_disabled()
        assert dashboard.is_time_range_visible()

        # Verify the dashboard table displays all expected columns
        assert dashboard.are_table_headers_visible()

        # Verify the canvases are visible for each table/graph panel
        assert dashboard.panels_are_rendered()

        # Verify there is dashboard data available in the results grid
        assert dashboard.get_visible_data_row_count() > 0

        # Basic interaction: scroll and verify UI remains responsive
        dashboard.scroll_dashboard()
        assert dashboard.is_home_header_visible()
