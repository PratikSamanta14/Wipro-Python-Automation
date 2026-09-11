from selenium import webdriver
from selenium.webdriver.common.by import By
import os


# Create Chrome WebDriver
driver = webdriver.Chrome()

try:

    # Get the path of index.html
    file_path = os.path.abspath("index.html")

    # Open the local HTML webpage
    driver.get("file:///" + file_path)

    print("Webpage opened successfully.")
    print("Page title:", driver.title)

    # -------------------------------------------------
    # 1. Locate Username field using By.ID
    # -------------------------------------------------

    username = driver.find_element(By.ID, "username")

    username.send_keys("Pratik")

    print("Username field located using By.ID")
    print("Username value:", username.get_attribute("value"))

    # -------------------------------------------------
    # 2. Locate Password field using By.NAME
    # -------------------------------------------------

    password = driver.find_element(By.NAME, "password")

    password.send_keys("test123")

    print("Password field located using By.NAME")
    print("Password value entered successfully.")

    # -------------------------------------------------
    # 3. Locate Selenium link using By.LINK_TEXT
    # -------------------------------------------------

    selenium_link = driver.find_element(
        By.LINK_TEXT,
        "Selenium Website"
    )

    print("Link located using By.LINK_TEXT")
    print("Link text:", selenium_link.text)

    # Display the URL of the link
    print("Link URL:", selenium_link.get_attribute("href"))

finally:

    # Close the browser
    driver.quit()

    print("Browser closed.")