import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# Function to read names from a file and return a random name
def get_random_name_from_file(file_path):
    with open(file_path, 'r') as file:
        # Read all lines and remove leading/trailing whitespaces
        names = [line.strip() for line in file.readlines() if line.strip()]
        # Return a random name from the list
        return random.choice(names) if names else None

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

    # Get a random name from the file 'first-names.txt'
    random_name = get_random_name_from_file('first-names.txt')

    if random_name:
        # Create the input string by adding the random name
        input_string = random_name

        # Locate the input field (First name field)
        first_name_input = driver.find_element(By.ID, "firstName")

        # Send the name to the input field
        first_name_input.send_keys(input_string)
        print(f"Sent the name: {input_string} to the First Name input field.")

        # Wait a bit to ensure the text is entered properly
        time.sleep(2)

        # Locate the "Next" button using its XPath
        next_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Next')]")

        # Click the "Next" button
        next_button.click()
        print("Clicked the 'Next' button.")

        # Wait for a bit to ensure the click is performed and the page loads
        time.sleep(5)

        # Take a full-screen screenshot of the page after filling the input field
        driver.save_screenshot("gmail_screenshot.png")
        print("Screenshot taken and saved as 'gmail_screenshot.png'")
    else:
        print("No names found in the file.")

finally:
    # Close the WebDriver
    driver.quit()

