"""
Login Page Object — handles Step 2: Login to application.

automationexercise.com has no pre-seeded demo account, so this page object
first tries to log in; if the account does not exist yet it transparently
signs one up (using data from testdata.json) and logs in with it. This
mirrors how a real first-run automation suite has to bootstrap test users.
"""
from selenium.webdriver.common.by import By

from config import config
from pages.base_page import BasePage


class LoginPage(BasePage):
    # --- Login form ---
    LOGIN_EMAIL = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    LOGIN_ERROR = (By.XPATH, "//p[contains(text(),'incorrect')]")

    # --- Signup form (same page, right-hand column) ---
    SIGNUP_NAME = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
    SIGNUP_EMAIL = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "button[data-qa='signup-button']")

    # --- Account information page ---
    PASSWORD = (By.ID, "password")
    DAYS = (By.ID, "days")
    MONTHS = (By.ID, "months")
    YEARS = (By.ID, "years")
    FIRST_NAME = (By.ID, "first_name")
    LAST_NAME = (By.ID, "last_name")
    ADDRESS1 = (By.ID, "address1")
    COUNTRY = (By.ID, "country")
    STATE = (By.ID, "state")
    CITY = (By.ID, "city")
    ZIPCODE = (By.ID, "zipcode")
    MOBILE_NUMBER = (By.ID, "mobile_number")
    CREATE_ACCOUNT_BUTTON = (By.CSS_SELECTOR, "button[data-qa='create-account']")
    ACCOUNT_CREATED_CONTINUE = (By.CSS_SELECTOR, "a[data-qa='continue-button']")

    def load(self):
        self.open(config.LOGIN_URL)
        self.dismiss_common_popups()
        return self

    def login(self, email: str, password: str):
        self.type_text(self.LOGIN_EMAIL, email)
        self.type_text(self.LOGIN_PASSWORD, password)
        self.click(self.LOGIN_BUTTON)
        return self

    def has_login_error(self) -> bool:
        return self.is_visible(self.LOGIN_ERROR, timeout=4)

    def start_signup(self, name: str, email: str):
        self.type_text(self.SIGNUP_NAME, name)
        self.type_text(self.SIGNUP_EMAIL, email)
        self.click(self.SIGNUP_BUTTON)
        return self

    def complete_account_information(self, account: dict):
        from selenium.webdriver.support.ui import Select

        self.type_text(self.PASSWORD, account["password"])
        Select(self.find(self.DAYS)).select_by_value(account["day"])
        Select(self.find(self.MONTHS)).select_by_visible_text(account["month"])
        Select(self.find(self.YEARS)).select_by_value(account["year"])

        self.type_text(self.FIRST_NAME, account["first_name"])
        self.type_text(self.LAST_NAME, account["last_name"])
        self.type_text(self.ADDRESS1, account["address1"])
        Select(self.find(self.COUNTRY)).select_by_visible_text(account["country"])
        self.type_text(self.STATE, account["state"])
        self.type_text(self.CITY, account["city"])
        self.type_text(self.ZIPCODE, account["zipcode"])
        self.type_text(self.MOBILE_NUMBER, account["mobile_number"])

        self.click(self.CREATE_ACCOUNT_BUTTON)
        self.click(self.ACCOUNT_CREATED_CONTINUE)
        return self

    def ensure_logged_in(self, account: dict):
        """
        Bootstraps and returns an authenticated session:
        try login -> on failure, sign up -> log in with the new account.
        """
        self.load()
        self.login(account["email"], account["password"])

        if self.has_login_error():
            self.load()
            self.start_signup(account["name"], account["email"])
            self.complete_account_information(account)
        return self
