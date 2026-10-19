from playwright.sync_api import Page, expect


class TodoPage:

    def __init__(self, page: Page):
        self.page = page

        self.new_todo = page.get_by_placeholder(
            "What needs to be done?"
        )

        self.todo_items = page.locator(
            ".todo-list li"
        )

    def open(self):
        self.page.goto(
            "https://demo.playwright.dev/todomvc/"
        )

    def add_todo(self, text):
        self.new_todo.fill(text)
        self.new_todo.press("Enter")

    def verify_todo(self, text):
        expect(
            self.page.get_by_text(text)
        ).to_be_visible()