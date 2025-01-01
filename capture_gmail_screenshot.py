import random
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# Function to read names from a file and return a random name
def get_random_name_from_file(file_path):
    with open(file_path, 'r') as file:
        # Read all lines and remove leading/trailing whitespaces
        names = [line.strip() for line in file.readlines() if line.strip()]
        # Return a random name from the list
        return random.choice(names) if names else None

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

# Function to click the "Next" button
def click_next_button():
    next_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Next')]")
    next_button.click()
    print("Clicked the 'Next' button.")

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

        # Click the "Next" button (after filling in the first name)
        click_next_button()

        # Wait for the page to load
        time.sleep(5)

        # Select a random month from the dropdown
        month_dropdown = Select(driver.find_element(By.ID, "month"))
        random_month = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])  # Random month from 1-12
        month_dropdown.select_by_value(str(random_month))
        print(f"Selected month: {random_month}")

        # Select a random day (1-31)
        random_day = random.randint(1, 31)
        day_input = driver.find_element(By.ID, "day")
        day_input.clear()  # Clear any pre-existing value
        day_input.send_keys(str(random_day))
        print(f"Entered day: {random_day}")

        # Select a random year (e.g., between 1990 and 2020)
        random_year = random.randint(1980, 1990)
        year_input = driver.find_element(By.ID, "year")
        year_input.clear()  # Clear any pre-existing value
        year_input.send_keys(str(random_year))
        print(f"Entered year: {random_year}")

        # Select a random gender between "Male" and "Female"
        gender_dropdown = Select(driver.find_element(By.ID, "gender"))
        random_gender = random.choice([1, 2])  # 1 for Male, 2 for Female
        gender_dropdown.select_by_value(str(random_gender))
        print(f"Selected gender: {'Male' if random_gender == 1 else 'Female'}")

        # Wait a bit to ensure the inputs are properly filled
        time.sleep(2)

        # Click the "Next" button again (after filling in the additional fields)
        click_next_button()

        # Wait for a bit to ensure the next step is loaded
        time.sleep(5)

        # Generate a random number with length 9
        random_number = generate_random_number(9)

        # Generate the username (name + random number)
        username = f"{input_string}{random_number}"

        # Locate the "Username" field and input the generated username
        username_input = driver.find_element(By.NAME, "Username")
        #username_input.clear()  # Clear any pre-existing value
        username_input.send_keys(username)
        print(f"Entered username: {username} into the 'Username' field.")

        # Wait a bit to ensure the input is filled
        time.sleep(2)

        # Click the "Next" button for the final time (after filling the username)
        click_next_button()

        # Wait for a bit to ensure the next step is loaded
        time.sleep(5)

        # Fill in the password field
        password = "Jelly90@@@"
        password_input = driver.find_element(By.NAME, "Passwd")
        password_input.clear()  # Clear any pre-existing value
        password_input.send_keys(password)
        print("Entered password: Jelly90@@@ into the 'Password' field.")

        # Fill in the confirm password field
        confirm_password_input = driver.find_element(By.NAME, "PasswdAgain")
        confirm_password_input.clear()  # Clear any pre-existing value
        confirm_password_input.send_keys(password)
        print("Entered password: Jelly90@@@ into the 'Confirm Password' field.")

        # Wait a bit to ensure the passwords are entered
        #time.sleep(2)

        # Click the "Next" button again after entering the password
        #click_next_button()

        # Wait for a bit to ensure the next step is loaded
        time.sleep(5)

        # Take a full-screen screenshot of the page after filling the input fields
        driver.save_screenshot("gmail_screenshot.png")
        print("Screenshot taken and saved as 'gmail_screenshot.png'")
    else:
        print("No names found in the file.")

finally:
    # Close the WebDriver
    driver.quit()
