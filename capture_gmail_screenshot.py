from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
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

    # Sleep for a few seconds to allow the page to fully load
    time.sleep(5)

    # Locate the "Create account" link by its visible text (or use any other selector)
    create_account_button = driver.find_element(By.XPATH, "//*[contains(text(), 'Create account')]")

    # Initialize ActionChains
    actions = ActionChains(driver)

    # Hover over the element
    actions.move_to_element(create_account_button).perform()

    # Sleep for a moment to ensure hover is done
    time.sleep(2)

    # Click the element
    actions.click(create_account_button).perform()

    # Wait for the page to load or respond after the click
    time.sleep(5)

    # Take a full-screen screenshot of the page after clicking
    driver.save_screenshot("gmail_screenshot_after_click.png")
    print("Screenshot taken and saved as 'gmail_screenshot_after_click.png'")

finally:
    # Close the WebDriver
    driver.quit()
