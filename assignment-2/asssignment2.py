from selenium import webdriver
from selenium.webdriver.common.by import By
import os


def main():

    # Open Chrome
    driver = webdriver.Chrome()

    try:

        # Open local HTML file
        driver.get("file:///" + os.path.abspath("index.html"))

        # 1. Locate element using ID
        title = driver.find_element(By.ID, "page-title")
        print("ID:", title.text)

        # 2. Locate element using NAME
        username = driver.find_element(By.NAME, "username")
        print("NAME:", username.get_attribute("placeholder"))

        # 3. Locate elements using CLASS_NAME
        cards = driver.find_elements(By.CLASS_NAME, "card")
        print("CLASS_NAME - Number of cards:", len(cards))

        # 4. Locate elements using TAG_NAME
        list_items = driver.find_elements(By.TAG_NAME, "li")
        print("TAG_NAME - Number of list items:", len(list_items))

        # 5. Locate element using LINK_TEXT
        selenium_link = driver.find_element(
            By.LINK_TEXT,
            "Selenium Official Website"
        )

        print("LINK_TEXT:", selenium_link.text)

        # 6. Locate element using PARTIAL_LINK_TEXT
        python_link = driver.find_element(
            By.PARTIAL_LINK_TEXT,
            "Python"
        )

        print("PARTIAL_LINK_TEXT:", python_link.text)

        # 7. Locate element using XPATH
        login_button = driver.find_element(
            By.XPATH,
            "//button[@id='login-btn']"
        )

        print("XPATH:", login_button.text)

        print("\nAssignment 2 completed successfully!")

    finally:

        # Close browser
        driver.quit()


if __name__ == "__main__":
    main()