"""
Screenshot + lightweight logging helpers used across the test flow.
Step 7 of the business flow: Capture screenshots.
"""
import os
from datetime import datetime

from config import config


def take_screenshot(driver, step_name: str) -> str:
    """Save a timestamped screenshot and return its file path."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_name = step_name.replace(" ", "_").lower()
    filename = f"{safe_name}_{timestamp}.png"
    filepath = os.path.join(config.SCREENSHOT_DIR, filename)
    driver.save_screenshot(filepath)
    print(f"[SCREENSHOT] {step_name} -> {filepath}")
    return filepath


def log_step(step_number: int, description: str) -> None:
    print(f"\n{'=' * 70}\nSTEP {step_number}: {description}\n{'=' * 70}")
