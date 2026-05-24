from pages.base_page import BasePage


class DashboardPage(BasePage):
    """Page object for the Grafana Synthetic Monitoring dashboard."""

    HOME_HEADING = "role=heading[name='Home']"
    SIGN_IN_LINK = "role=link[name='Sign in']"
    CHECKS_GRID = "role=grid"
    SEARCH_BUTTON = "role=button[name='Search...']"
    FILTER_BUTTON = "role=button[name='Add filter']"
    ALERT_FIRING_LABEL = "label[data-testid='data-testid Dashboard template variables submenu Label Alert firing']"
    ALERT_PENDING_LABEL = "label[data-testid='data-testid Dashboard template variables submenu Label Alert pending']"
    REGION_FILTER_LABEL = "label[data-testid='data-testid Dashboard template variables submenu Label region']"
    PROBE_FILTER_LABEL = "label[data-testid='data-testid Dashboard template variables submenu Label probe']"
    CREATE_NEW_CHECK_LINK = "a:has-text('Create new check')"
    TIME_RANGE_BUTTON = "role=button[name='Time range selected: Last 3 hours']"
    PANEL_CONTENT = "div[data-testid='data-testid panel content']"
    CHECK_TYPE_FILTER_LABEL = "label[data-testid='data-testid Dashboard template variables submenu Label check type']"
    EXPECTED_TABLE_HEADERS = [
        'id',
        'instance',
        'job',
        'check type',
        'state',
        'reachability',
        'latency',
    ]
    DASHBOARD_HEADINGS = [
    "All checks",
    "All error rate by location",
    "All check error percentage",
    "All latency",
    ]

    def wait_for_dashboard(self):
        self.page.wait_for_selector(self.HOME_HEADING)
        self.page.wait_for_selector(self.CHECKS_GRID)
        self.page.wait_for_selector(self.SIGN_IN_LINK)

    def click_check_type_dropdown(self) -> None:
        self.page.locator(
            '[data-testid="data-testid template variable"]'
        ).filter(
            has=self.page.locator(self.CHECK_TYPE_FILTER_LABEL)
        ).get_by_role("combobox").click()

    def are_dashboard_headings_visible(self) -> bool:
        return all(
            self.page.get_by_role("heading", name=h).is_visible()
            for h in self.DASHBOARD_HEADINGS
    )

    def is_home_header_visible(self) -> bool:
        return self.page.locator(self.HOME_HEADING).is_visible()

    def is_search_visible(self) -> bool:
        return self.page.locator(self.SEARCH_BUTTON).is_visible()

    def is_filter_button_visible(self) -> bool:
        return self.page.locator(self.FILTER_BUTTON).is_visible()

    def is_alert_firing_visible(self) -> bool:
        return self.page.locator(self.ALERT_FIRING_LABEL).is_visible()

    def is_alert_pending_visible(self) -> bool:
        return self.page.locator(self.ALERT_PENDING_LABEL).is_visible()

    def is_region_filter_visible(self) -> bool:
        return self.page.locator(self.REGION_FILTER_LABEL).is_visible()

    def is_probe_filter_visible(self) -> bool:
        return self.page.locator(self.PROBE_FILTER_LABEL).is_visible()

    def is_check_type_filter_visible(self) -> bool:
        return self.page.locator(self.CHECK_TYPE_FILTER_LABEL).is_visible()

    def is_create_new_check_disabled(self) -> bool:
        locator = self.page.locator(self.CREATE_NEW_CHECK_LINK).first
        return locator.get_attribute('aria-disabled') == 'true' or not locator.is_enabled()

    def is_time_range_visible(self) -> bool:
        return self.page.locator(self.TIME_RANGE_BUTTON).is_visible()

    def are_table_headers_visible(self) -> bool:
        for header in self.EXPECTED_TABLE_HEADERS:
            locator = self.page.get_by_role('columnheader', name=header)
            if locator.count() == 0 or not locator.first.is_visible():
                return False
        return True

    def get_visible_data_row_count(self) -> int:
        rows = self.page.get_by_role('row')
        count = rows.count()
        return count - 1 if count > 1 else count

    def scroll_dashboard(self, delta_y: int = 500):
        self.page.mouse.wheel(0, delta_y)

    def are_filters_visible(self) -> bool:
        return (
            self.is_filter_button_visible() and
            self.is_alert_firing_visible() and
            self.is_alert_pending_visible() and
            self.is_region_filter_visible() and
            self.is_probe_filter_visible() and
            self.is_check_type_filter_visible()
    )

    def get_visible_dashboard_headings(self) -> list[str]:
        return [heading.inner_text().strip() for heading in self.page.get_by_role("heading").all()]

    def filtered_headings_match(self, filter_value: str) -> bool:
        expected_headings = [
            heading.replace("All", filter_value, 1) if heading.startswith("All") else heading
            for heading in self.DASHBOARD_HEADINGS
        ]
        actual_texts = [text.lower() for text in self.get_visible_dashboard_headings()]
        return all(any(expected.lower() in actual for actual in actual_texts) for expected in expected_headings)

    def wait_for_filtered_headings(self, filter_value: str, timeout: int = 15000) -> None:
        expected_headings = [
            heading.replace("All", filter_value, 1) if heading.startswith("All") else heading
            for heading in self.DASHBOARD_HEADINGS
        ]
        self.page.wait_for_function(
            "(expected) => {"
            "  const visible = [...document.querySelectorAll('h1,h2,h3,h4,h5,h6')]"
            "    .map(el => el.textContent.trim().toLowerCase());"
            "  return expected.every(exp => visible.some(text => text.includes(exp.toLowerCase())));"
            "}",
            arg=expected_headings,
            timeout=timeout,
        )

    def panels_are_rendered(self):
        panels = self.page.locator(self.PANEL_CONTENT)

        assert panels.count() >= len(self.DASHBOARD_HEADINGS)

        for panel in panels.all():
            has_canvas = panel.locator("canvas").count() > 0
            has_svg = panel.locator("svg").count() > 0
            has_table = panel.locator("table").count() > 0
            has_grid = panel.get_by_role('grid').count() > 0
            if not (has_canvas or has_svg or has_table or has_grid):
                return False
        return True

    def search_and_wait_for_heading(self, query: str, heading_text: str | None = "Observability", target_path: str | None = "/observability", timeout: int = 30000) -> None:
        self.page.locator(self.SEARCH_BUTTON).click()
        # Try to find a visible search input that appears after clicking the button.
        input_selectors = (
            'input[aria-label*="Search"]',
            'input[placeholder*="Search"]',
            'input[type="search"]',
            'input[role="combobox"]',
        )

        input_found = False
        for sel in input_selectors:
            try:
                self.page.wait_for_selector(sel + ':visible', timeout=3000)
                search_input = self.page.locator(sel).first
                search_input.click()
                search_input.fill(query)
                search_input.press('Enter')
                input_found = True
                break
            except Exception:
                continue

        # If no input appeared, use global keyboard
        if not input_found:
            self.page.keyboard.type(query)
            self.page.keyboard.press("Enter")

        # wait for navigation target
        if target_path:
            self.page.wait_for_url(f"**{target_path}", timeout=timeout)

        # wait for heading
        if heading_text:
            self.page.get_by_role("heading", name=heading_text).wait_for(state="visible", timeout=timeout)