from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class SecurePage(BasePage):

    URL = "https://practice.expandtesting.com/secure"

    def __init__(self, page: Page):
        super().__init__(page)

        self.success_message = page.get_by_text(
            "You logged into a secure area!"
        )

        self.logout_button = page.get_by_role(
            "link",
            name="Logout"
        )

    def verify_login_successful(self):
        expect(self.page).to_have_url(self.URL)
        expect(self.success_message).to_be_visible()