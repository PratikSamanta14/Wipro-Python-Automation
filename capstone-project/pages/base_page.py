"""
Base Page Object.
Holds every reusable Selenium action so individual page classes stay thin.
Also centralizes Step 9: Handle popup/alerts if available.
"""
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    NoAlertPresentException,
    NoSuchElementException,
    TimeoutException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import config


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, config.EXPLICIT_WAIT)

    # ---- generic actions ----------------------------------------------------
    def open(self, url: str):
        self.driver.get(url)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        """
        Click with resilience against third-party ad/overlay elements that
        automationexercise.com occasionally injects mid-test (e.g. Google
        ad iframes), which can intercept a plain .click() call.
        """
        element = self.find_clickable(locator)
        self.scroll_to(element)
        try:
            element.click()
        except ElementClickInterceptedException:
            print(f"[CLICK] Normal click intercepted on {locator}; removing overlays and retrying via JS.")
            self.remove_ad_overlays()
            self.driver.execute_script("arguments[0].click();", element)

    def type_text(self, locator, text: str, clear_first: bool = True):
        element = self.find(locator)
        if clear_first:
            element.clear()
        element.send_keys(text)

    def is_visible(self, locator, timeout: int = 5) -> bool:
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def get_text(self, locator) -> str:
        return self.find(locator).text.strip()

    def scroll_to(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def remove_ad_overlays(self):
        """
        automationexercise.com serves live Google ad slots (iframes whose
        id/name starts with 'aswift_' or 'google_ads_iframe') that can
        render on top of real page elements at unpredictable times. Since
        we don't control or need them, the safest fix is to strip them
        from the DOM via JS rather than guess at a close button.
        """
        self.driver.execute_script(
            """
            document.querySelectorAll(
                "iframe[id^='aswift_'], iframe[id^='google_ads_iframe'], ins.adsbygoogle, div[id^='div-gpt-ad']"
            ).forEach(el => el.remove());
            """
        )

    # ---- Step 9: popup / alert handling --------------------------------------
    def handle_js_alert(self, accept: bool = True):
        """Accept or dismiss a native JS alert/confirm/prompt if one is present."""
        try:
            alert = self.wait.until(EC.alert_is_present())
            text = alert.text
            alert.accept() if accept else alert.dismiss()
            print(f"[ALERT] Handled JS alert with text: '{text}'")
            return text
        except (TimeoutException, NoAlertPresentException):
            return None

    def dismiss_common_popups(self):
        """
        Best-effort dismissal of cookie-consent banners / ad overlays that
        third-party demo sites occasionally inject. Every attempt is wrapped
        so a missing popup never fails the test.
        """
        self.remove_ad_overlays()

        candidate_selectors = [
            (By.CSS_SELECTOR, "button[aria-label='Close']"),
            (By.CSS_SELECTOR, ".fc-cta-consent"),
            (By.CSS_SELECTOR, "#close_btn"),
            (By.CSS_SELECTOR, ".close-btn"),
            (By.XPATH, "//button[contains(., 'Accept') or contains(., 'Consent')]"),
            (By.XPATH, "//div[@id='ad_position_box']//button"),
        ]
        for locator in candidate_selectors:
            try:
                elements = self.driver.find_elements(*locator)
                for el in elements:
                    if el.is_displayed():
                        el.click()
                        print(f"[POPUP] Dismissed popup via {locator}")
            except (NoSuchElementException, Exception):
                continue

        # Also swallow any stray native alert that might be blocking the page.
        self.handle_js_alert(accept=True)