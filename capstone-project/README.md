# Capstone Project — E-Commerce Automation with Selenium WebDriver (Python)

Automates the customer purchase journey on **[automationexercise.com](https://automationexercise.com)**
using the Page Object Model, pytest, and data-driven inputs from JSON + Excel.

## Project structure

```
capstone-ecommerce-automation/
├── config/
│   └── config.py            # URLs, timeouts, folder paths
├── data/
│   ├── testdata.json        # account info, search terms
│   └── testdata.xlsx        # SearchData sheet (TestCaseID, SearchTerm, ExpectedQuantity)
├── pages/
│   ├── base_page.py         # shared waits/clicks + popup & alert handling
│   ├── login_page.py        # login + auto-signup
│   ├── home_page.py         # product search
│   ├── product_page.py      # quantity update + add-to-cart
│   └── cart_page.py         # cart verification
├── tests/
│   ├── conftest.py          # driver fixture, data fixtures, failure screenshots
│   └── test_ecommerce_flow.py
├── utils/
│   ├── driver_factory.py    # Chrome/Firefox WebDriver setup
│   ├── data_reader.py       # JSON + Excel readers
│   └── report_helper.py     # screenshot + logging helpers
├── screenshots/              # generated at runtime
├── reports/                   # generated at runtime (pytest-html)
├── requirements.txt
├── pytest.ini
└── .gitignore
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Chrome and Firefox binaries are the only local dependencies — `webdriver-manager`
downloads the matching driver automatically on first run.

## Run

```bash
pytest
```

- Headless / CI mode: `HEADLESS=true pytest`
- Firefox instead of Chrome: `BROWSER=firefox pytest`
- HTML execution report: generated at `reports/execution_report.html`
  (self-contained — open it directly in a browser).
- Screenshots: saved to `screenshots/` at every major step, plus automatically
  on any test failure (see `conftest.py`).

## How each capstone requirement is covered

| # | Requirement | Where |
|---|---|---|
| 1 | Launch browser | `utils/driver_factory.py`, `driver` fixture in `conftest.py` |
| 2 | Login to application | `pages/login_page.py` — tries login, auto-signs-up a fresh account on first run (the demo site has no pre-seeded account) |
| 3 | Search product | `pages/home_page.py::search_product` |
| 4 | Add product to cart | `pages/product_page.py::add_to_cart` |
| 5 | Update quantity | `pages/product_page.py::set_quantity` (set on the product detail page before adding to cart) |
| 6 | Verify cart details | `pages/cart_page.py::verify_item_in_cart` |
| 7 | Capture screenshots | `utils/report_helper.py::take_screenshot`, called at every stage + on failure |
| 8 | Read test data from Excel/JSON | `utils/data_reader.py` — account info & search-term list from `testdata.json`, the driven search term/quantity for the run from `testdata.xlsx` |
| 9 | Handle popup/alerts | `pages/base_page.py::dismiss_common_popups` and `handle_js_alert`, applied on page loads and after the "Added!" add-to-cart modal |
| 10 | Generate execution report | `pytest-html`, configured in `pytest.ini` (`--html=reports/execution_report.html`) |

## Notes

- The site is a public community demo app; its DOM occasionally changes. If a
  locator breaks, the affected selector is isolated in exactly one page-object
  class, per the Page Object Model, so the fix is localized.
- A fresh email is generated per run (`utils/data_reader.py`) since
  automationexercise.com rejects duplicate sign-ups.
- To extend to `demo.opencart.com` or `tutorialsninja.com` instead, only
  `config/config.py` and the locators inside `pages/` need to change — the
  test flow and data layer stay the same.
