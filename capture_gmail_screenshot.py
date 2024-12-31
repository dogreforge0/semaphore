import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# Function to generate a random number with a length of 9
def generate_random_number(length=9):
    return ''.join(random.choices('0123456789', k=length))

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

    # Generate a random number with length 9
    random_number = generate_random_number(9)

    # Create the string to send: 'ponytech' + random number
    input_string = f"ponytech{random_number}"

    # Locate the input field (First name field)
    first_name_input = driver.find_element(By.ID, "firstName")

    # Send the string to the input field
    first_name_input.send_keys(input_string)
    print(f"Sent the string: {input_string} to the First Name input field.")

    # Wait a bit to ensure the text is entered properly
    time.sleep(2)

    # Take a full-screen screenshot of the page after filling the input field
    driver.save_screenshot("gmail_screenshot_after_input.png")
    print("Screenshot taken and saved as 'gmail_screenshot_after_input.png'")

finally:
    # Close the WebDriver
    driver.quit()
