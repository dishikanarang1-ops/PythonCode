from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class LoginPage(BasePage):

    URL = "https://practice.expandtesting.com/login"

    def __init__(self, page: Page):
        super().__init__(page)

        # Locators
        self.username = page.get_by_label("Username")
        self.password = page.get_by_label("Password")

        self.login_button = page.get_by_role(
            "button",
            name="Login"
        )

        self.error_message = page.locator("#flash")

    def open(self):
        self.navigate(self.URL)

    def login(self, username: str, password: str):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()

    def verify_login_failed(self):
        expect(self.error_message).to_be_visible()