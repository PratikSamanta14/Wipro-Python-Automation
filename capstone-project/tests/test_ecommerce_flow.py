"""
Capstone Project: Automate an E-Commerce Web Application using Selenium WebDriver + Python.

Business scenario covered end-to-end in a single ordered flow:
 1. Launch browser                    -> driver fixture (conftest.py)
 2. Login to application              -> LoginPage.ensure_logged_in()
 3. Search product                    -> HomePage.search_product()
 4. Add product to cart               -> ProductPage.add_to_cart()
 5. Update quantity                   -> ProductPage.set_quantity()
 6. Verify cart details               -> CartPage.verify_item_in_cart()
 7. Capture screenshots               -> take_screenshot() at every stage
 8. Read test data from Excel/JSON    -> excel_data / json_data fixtures
 9. Handle popup/alerts               -> BasePage.dismiss_common_popups()
10. Generate execution report         -> pytest-html (see pytest.ini)

Run with:  pytest tests/test_ecommerce_flow.py
Report:    reports/execution_report.html
"""
import pytest

from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from utils.report_helper import log_step, take_screenshot


@pytest.mark.regression
def test_search_add_to_cart_and_verify(driver, json_data, excel_data):
    account = json_data["account"]

    # Data-driven: pull the primary scenario row from the Excel sheet.
    scenario = excel_data[0]
    search_term = scenario["SearchTerm"]
    expected_quantity = int(scenario["ExpectedQuantity"])

    # ---- Step 1 & 2: Launch browser (fixture) + Login -----------------------
    log_step(1, "Launch browser")
    log_step(2, "Login to application (auto-signup on first run)")
    login_page = LoginPage(driver)
    login_page.ensure_logged_in(account)
    take_screenshot(driver, "01_after_login")

    home_page = HomePage(driver)
    assert home_page.is_logged_in(), "Login/signup did not succeed."

    # ---- Step 3: Search product ----------------------------------------------
    log_step(3, f"Search product: '{search_term}'")
    home_page.search_product(search_term)
    take_screenshot(driver, "02_search_results")
    assert home_page.get_search_result_count() > 0, f"No results found for '{search_term}'."

    home_page.open_first_result()

    # ---- Step 5: Update quantity (set before adding to cart) -----------------
    log_step(5, f"Update quantity to {expected_quantity}")
    product_page = ProductPage(driver)
    product_name = product_page.get_product_name()
    product_page.set_quantity(expected_quantity)
    take_screenshot(driver, "03_quantity_updated")

    # ---- Step 4: Add product to cart ------------------------------------------
    log_step(4, "Add product to cart")
    product_page.add_to_cart()
    take_screenshot(driver, "04_added_to_cart_modal")

    # ---- Step 9: Handle popup/alerts (post add-to-cart modal) -----------------
    log_step(9, "Handle popup/alerts")
    product_page.go_to_cart_from_modal()

    # ---- Step 6: Verify cart details -------------------------------------------
    log_step(6, "Verify cart details")
    cart_page = CartPage(driver)
    cart_page.dismiss_common_popups()
    take_screenshot(driver, "05_cart_page")

    cart_items = cart_page.get_cart_items()
    print(f"[CART] Items found: {cart_items}")

    assert len(cart_items) > 0, "Cart is empty after add-to-cart."
    assert cart_page.verify_item_in_cart(
        product_name, expected_quantity
    ), f"Expected '{product_name}' with quantity {expected_quantity} in cart."

    take_screenshot(driver, "06_verification_complete")
    print(f"[PASS] '{product_name}' verified in cart with quantity {expected_quantity}.")
