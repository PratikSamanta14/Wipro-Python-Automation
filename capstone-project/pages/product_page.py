"""
Product Detail Page Object.
Handles Step 4: Add product to cart, and Step 5: Update quantity.
"""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductPage(BasePage):
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product-information h2")
    QUANTITY_INPUT = (By.ID, "quantity")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".product-information button.cart")
    CONTINUE_SHOPPING_BUTTON = (By.XPATH, "//button[contains(text(),'Continue Shopping')]")
    VIEW_CART_LINK = (By.XPATH, "//u[text()='View Cart']")

    def get_product_name(self) -> str:
        # Collapse any incidental double spaces from the site's markup so the
        # name compares cleanly against the cart page later.
        return " ".join(self.get_text(self.PRODUCT_NAME).split())

    def set_quantity(self, quantity: int):
        """Step 5: Update quantity before adding the item to the cart."""
        quantity_field = self.find(self.QUANTITY_INPUT)
        quantity_field.clear()
        quantity_field.send_keys(str(quantity))
        return self

    def add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)
        # A modal ("Added!") pops up after adding — this IS one of the
        # popups Step 9 asks us to handle.
        if self.is_visible(self.CONTINUE_SHOPPING_BUTTON, timeout=6):
            pass  # modal confirmed present; caller decides continue vs view cart
        return self

    def go_to_cart_from_modal(self):
        self.click(self.VIEW_CART_LINK)
        return self

    def continue_shopping_from_modal(self):
        self.click(self.CONTINUE_SHOPPING_BUTTON)
        return self