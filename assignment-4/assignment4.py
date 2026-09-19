from selenium import webdriver
from selenium.webdriver.common.by import By
import os


def main():

    # Open Chrome
    driver = webdriver.Chrome()

    try:

        # Open local HTML file
        driver.get("file:///" + os.path.abspath("index.html"))

        # 1. Absolute XPath
        heading = driver.find_element(
            By.XPATH,
            "/html/body/h1"
        )

        print("Absolute XPath:", heading.text)

        # 2. Relative XPath
        books = driver.find_elements(
            By.XPATH,
            "//div[@class='book']"
        )

        print(
            "Relative XPath - Number of books:",
            len(books)
        )

        # 3. Attribute-based XPath
        selenium_book = driver.find_element(
            By.XPATH,
            "//div[@data-id='101']/h2"
        )

        print(
            "Attribute XPath:",
            selenium_book.text
        )

        # 4. XPath indexing
        second_book = driver.find_element(
            By.XPATH,
            "(//div[@class='book'])[2]/h2"
        )

        print(
            "Indexing [2]:",
            second_book.text
        )

        # 5. Parent-child XPath
        author = driver.find_element(
            By.XPATH,
            "//div[@data-id='101']/p[@class='author']"
        )

        print(
            "Parent-child XPath:",
            author.text
        )

        # 6. Stable attribute
        python_book = driver.find_element(
            By.XPATH,
            "//div[@data-id='102']"
        )

        print(
            "Stable attribute:",
            python_book.get_attribute("data-id")
        )

        print("\nAssignment 4 completed successfully!")

    finally:

        # Close browser
        driver.quit()


if __name__ == "__main__":
    main()