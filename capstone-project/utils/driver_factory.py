"""
Creates and configures the WebDriver instance.
Uses webdriver-manager so no manual driver binaries are needed.
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from config import config


def get_driver(browser: str = None, headless: bool = None):
    """
    Step 1 of the business flow: Launch browser.
    Returns a ready-to-use, maximized WebDriver instance.
    """
    browser = (browser or config.BROWSER).lower()
    headless = config.HEADLESS if headless is None else headless

    if browser == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options,
        )
    else:  # default: chrome
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-infobars")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options,
        )

    driver.implicitly_wait(config.IMPLICIT_WAIT)
    if not headless:
        driver.maximize_window()
    return driver
