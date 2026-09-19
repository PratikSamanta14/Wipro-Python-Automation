"""
Shared pytest fixtures for the capstone suite.
"""
import pytest

from utils.data_reader import read_excel_data, read_json_data
from utils.driver_factory import get_driver
from utils.report_helper import take_screenshot


@pytest.fixture(scope="function")
def driver():
    """Step 1: Launch browser. Quits automatically after the test."""
    drv = get_driver()
    yield drv
    drv.quit()


@pytest.fixture(scope="session")
def json_data():
    return read_json_data()


@pytest.fixture(scope="session")
def excel_data():
    return read_excel_data()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Automatically capture a screenshot whenever a test fails, and embed it
    into the pytest-html execution report (Step 7 + Step 10 tie-in).
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver is not None:
            take_screenshot(driver, f"FAILURE_{item.name}")
