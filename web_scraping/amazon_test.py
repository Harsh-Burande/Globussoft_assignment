from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from datetime import datetime

driver = webdriver.Chrome()

driver.get("https://www.amazon.in/s?k=laptop&crid=AKKWG9KT7BGM&sprefix=%2Caps%2C353&ref=nb_sb_ss_recent_1_0_recent")

# Wait for page to load
time.sleep(5)

# Find all the products on the page
products = driver.find_elements(
    By.CSS_SELECTOR,
    '[data-component-type="s-search-result"]'
)

print("Product found...", len(products))

# Empty list to store the data
data = []

# Iterate through the products and print their names and prices
for i, product in enumerate(products, start=1):
    try:
        title = product.find_element(
            By.TAG_NAME,
            "h2"
        ).text

        price = product.find_element(
            By.CLASS_NAME,
            "a-price-whole"
        ).text

        try:
            rating_text = product.find_element(
                By.CSS_SELECTOR,
                'a[aria-label*="out of 5 stars"]'
            ).get_attribute("aria-label")

            rating = rating_text.split("out of")[0]
        except:
            rating = "Not Available"
        
        try:
            image_url = product.find_element(
                By.CSS_SELECTOR,
                "img"
            ).get_attribute("src")
        except:
            image_url = "Not Available"

        if "Sponsored" in product.text:
            result_type = "Ad"
        else:
            result_type = "Organic"

        print(f"{i}")
        print(f"{title}")
        print(f"{price}")
        print(f"{rating}")
        print(f"{image_url}")
        print(f"{result_type}")
        print("-" * 50  )

    except Exception as e:
        print(f"{i}. Error")
        print(e)

    data.append({
        "Image":image_url,
        "Title":title,
        "Price":price,
        "Rating":rating,
        "Result_Type":result_type
    })

# Save the data to a CSV file
dataframe = pd.DataFrame(data)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

filename = f"amazon_laptops_{timestamp}.csv"

dataframe.to_csv(filename, index=False)

print(f"Data saved to {filename}")

driver.quit()