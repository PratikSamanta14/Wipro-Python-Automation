"""
Home Page Object — handles Step 3: Search product.
"""
from selenium.webdriver.common.by import By

from config import config
from pages.base_page import BasePage


class HomePage(BasePage):
    SEARCH_BOX = (By.ID, "search_product")
    SEARCH_BUTTON = (By.ID, "submit_search")
    SEARCHED_PRODUCTS_TITLE = (By.XPATH, "//h2[text()='Searched Products']")
    PRODUCT_CARDS = (By.CSS_SELECTOR, ".features_items .product-image-wrapper")
    LOGGED_IN_AS = (By.XPATH, "//a[contains(text(),'Logged in as')]")

    def load(self):
        self.open(config.BASE_URL)
        self.dismiss_common_popups()
        return self

    def is_logged_in(self) -> bool:
        return self.is_visible(self.LOGGED_IN_AS, timeout=5)

    def go_to_products_page(self):
        """
        The search box (#search_product) only exists on the Products
        listing page, not on the homepage — navigate there explicitly
        before attempting to search.
        """
        self.open(config.PRODUCTS_URL)
        self.dismiss_common_popups()
        return self

    def search_product(self, product_name: str):
        self.go_to_products_page()
        self.click(self.SEARCH_BOX)
        self.type_text(self.SEARCH_BOX, product_name)
        self.click(self.SEARCH_BUTTON)
        self.wait.until(lambda d: self.is_visible(self.SEARCHED_PRODUCTS_TITLE, timeout=10))
        return self

    def get_search_result_count(self) -> int:
        return len(self.driver.find_elements(*self.PRODUCT_CARDS))

    def open_first_result(self):
        """Click 'View Product' on the first card returned by the search."""
        first_card = self.driver.find_elements(*self.PRODUCT_CARDS)[0]
        self.scroll_to(first_card)
        view_link = first_card.find_element(By.CSS_SELECTOR, "a[href*='/product_details/']")
        view_link.click()
        return self