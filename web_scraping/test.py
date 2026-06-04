from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.google.com")
input("Press enter to close the browser...")
driver.quit()