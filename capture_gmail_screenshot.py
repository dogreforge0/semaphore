from selenium import webdriver
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

    # Find all elements on the page and print their full HTML structure
    elements = driver.find_elements(By.XPATH, "//*")
    for element in elements:
        # Print the HTML structure of the element (including its tag, attributes, and inner HTML)
        html_content = element.get_attribute('outerHTML')
        print(html_content)

    time.sleep(2)
    
    # Take a full-screen screenshot of the page
    driver.save_screenshot("gmail_screenshot.png")
    print("Screenshot taken and saved as 'gmail_screenshot.png'")

finally:
    # Close the WebDriver
    driver.quit()
