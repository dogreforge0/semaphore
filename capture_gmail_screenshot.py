from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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

    # Get the full HTML content of the page
    page_html = driver.page_source

    # Save the HTML to a text file
    with open("gmail_page_content.txt", "w") as file:
        file.write(page_html)
    
    print("HTML content saved to 'gmail_page_content.txt'")

    time.sleep(2)

    # Take a screenshot of the page and save it
    driver.save_screenshot("gmail_screenshot.png")
    print("Screenshot taken and saved as 'gmail_screenshot.png'")

finally:
    # Close the WebDriver
    driver.quit()
