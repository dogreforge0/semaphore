from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    # Wait for the "Create account" button to be clickable
    create_account_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Create account']"))
    )
    
    # Click on the "Create account" button
    create_account_button.click()
    print("Clicked on the 'Create account' button")
    
    # Wait for a few seconds to let the page load after clicking
    time.sleep(5)
    
    # Take a full-screen screenshot of the page after clicking the button
    driver.save_screenshot("gmail_screenshot.png")
    print("Screenshot taken and saved as 'gmail_screenshot.png'")

finally:
    # Close the WebDriver
    driver.quit()
