from selenium import webdriver
from selenium.webdriver.common.by import By
import os


def main():

    # Open Chrome
    driver = webdriver.Chrome()

    try:

        # Open local HTML file
        driver.get("file:///" + os.path.abspath("index.html"))

        # 1. ID selector
        heading = driver.find_element(
            By.CSS_SELECTOR,
            "#heading"
        )

        print("ID selector:", heading.text)

        # 2. Class selector
        items = driver.find_elements(
            By.CSS_SELECTOR,
            ".item"
        )

        print("Class selector - Number of items:", len(items))

        # 3. Tag selector
        inputs = driver.find_elements(
            By.CSS_SELECTOR,
            "input"
        )

        print("Tag selector - Number of inputs:", len(inputs))

        # 4. Parent > Child selector
        child = driver.find_element(
            By.CSS_SELECTOR,
            "#parent > .child"
        )

        print("Parent > Child:", child.text)

        # 5. Attribute selector
        username = driver.find_element(
            By.CSS_SELECTOR,
            "input[name='username']"
        )

        print(
            "Attribute selector:",
            username.get_attribute("name")
        )

        # 6. *= Contains
        selenium_item = driver.find_element(
            By.CSS_SELECTOR,
            "[data-name*='selenium']"
        )

        print("*= selector:", selenium_item.text)

        # 7. ^= Starts with
        email = driver.find_element(
            By.CSS_SELECTOR,
            "input[name^='user']"
        )

        print(
            "^= selector:",
            email.get_attribute("name")
        )

        # 8. $= Ends with
        user_email = driver.find_element(
            By.CSS_SELECTOR,
            "input[name$='email']"
        )

        print(
            "$= selector:",
            user_email.get_attribute("name")
        )

        print("\nAssignment 3 completed successfully!")

    finally:

        # Close browser
        driver.quit()


if __name__ == "__main__":
    main()