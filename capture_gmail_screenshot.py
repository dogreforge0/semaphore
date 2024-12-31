from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Setup Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--window-size=1920x1080")

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open Gmail login page
    driver.get("https://mail.google.com/")

    # Wait for Gmail to load
    time.sleep(5)

    # Take a screenshot of the page
    driver.save_screenshot("gmail_screenshot.png")
    print("Screenshot taken and saved as 'gmail_screenshot.png'")

finally:
    driver.quit()
