"""
Central configuration for the capstone automation suite.
Values can be overridden with environment variables so the same
codebase runs unchanged in CI (headless) or locally (headed).
"""
import os

# ---- Application under test -------------------------------------------------
BASE_URL = os.getenv("BASE_URL", "https://automationexercise.com")
LOGIN_URL = f"{BASE_URL}/login"
PRODUCTS_URL = f"{BASE_URL}/products"
CART_URL = f"{BASE_URL}/view_cart"

# ---- Browser ------------------------------------------------------------------
BROWSER = os.getenv("BROWSER", "chrome")          # chrome | firefox
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
IMPLICIT_WAIT = 5
EXPLICIT_WAIT = 15

# ---- Folders --------------------------------------------------------------
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(ROOT_DIR, "data")
SCREENSHOT_DIR = os.path.join(ROOT_DIR, "screenshots")
REPORT_DIR = os.path.join(ROOT_DIR, "reports")

JSON_DATA_FILE = os.path.join(DATA_DIR, "testdata.json")
EXCEL_DATA_FILE = os.path.join(DATA_DIR, "testdata.xlsx")

os.makedirs(SCREENSHOT_DIR, exist_ok=True)
os.makedirs(REPORT_DIR, exist_ok=True)