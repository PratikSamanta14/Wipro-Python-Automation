"""
Cart Page Object — handles Step 6: Verify cart details.
"""
from selenium.webdriver.common.by import By

from config import config
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ROWS = (By.CSS_SELECTOR, "#cart_info_table tbody tr")

    def load(self):
        self.open(config.CART_URL)
        self.dismiss_common_popups()
        return self

    def get_cart_items(self) -> list:
        """
        Returns cart contents as a list of dicts:
        [{'name': ..., 'price': ..., 'quantity': ..., 'total': ...}, ...]
        """
        items = []
        rows = self.driver.find_elements(*self.CART_ROWS)
        for row in rows:
            name = row.find_element(By.CSS_SELECTOR, "td.cart_description h4 a").text.strip()
            price = row.find_element(By.CSS_SELECTOR, "td.cart_price p").text.strip()
            quantity = row.find_element(
                By.CSS_SELECTOR, "td.cart_quantity button"
            ).text.strip()
            total = row.find_element(By.CSS_SELECTOR, "td.cart_total p").text.strip()
            items.append(
                {"name": name, "price": price, "quantity": quantity, "total": total}
            )
        return items

    def verify_item_in_cart(self, product_name: str, expected_quantity: int) -> bool:
        # Normalize whitespace: automationexercise.com's product-detail title
        # occasionally has double spaces (HTML source formatting) while the
        # cart page renders the same name with single spaces.
        target = " ".join(product_name.lower().split())
        for item in self.get_cart_items():
            cart_name = " ".join(item["name"].lower().split())
            if cart_name == target:
                return int(item["quantity"]) == expected_quantity
        return False