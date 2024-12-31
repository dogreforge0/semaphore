from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Setup Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no GUI)
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--window-size=1920x1080")  # Set the initial window size (for headless mode)

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open Gmail login page
    driver.get("https://mail.google.com/")
    
    # Maximize the window to full screen for better screenshot capture
    driver.maximize_window()

    # Sleep for a few seconds to allow the page to fully load
    time.sleep(5)

    # Find the body element to send TAB keys
    body = driver.find_element(By.TAG_NAME, "body")

    # Send TAB key five times with a delay after each press
    for _ in range(5):
        body.send_keys(Keys.TAB)
        time.sleep(1)  # Delay of 1 second between each TAB key press

    # After sending TAB keys, press Enter to interact with the focused element
    body.send_keys(Keys.ENTER)

    # Wait a few seconds to ensure the page responds after pressing Enter
    time.sleep(5)

    # Take a full-screen screenshot of the page
    driver.save_screenshot("gmail_screenshot.png")
    print("Screenshot taken and saved as 'gmail_screenshot.png'")

finally:
    # Close the WebDriver
    driver.quit()
