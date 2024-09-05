from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import schedule


def smallest(list_of_elements):
    """Takes the list of elements and returns the index of the smallest positive value"""
    index = ""
    small = list_of_elements[0]
    for count, elements in enumerate(list_of_elements):
        # Check if the element is a positive number and smaller than the current smallest value
        if 0 < elements < small:
            small = elements
            index = list_of_elements.index(elements)
    return index


# Function to check if items can be bought with available money
def checker(list_of_items, prices_of_items):
    # Get the current amount of money available
    money = driver.find_element(By.ID, "money")
    no_of_coins = money.text

    # Remove commas from the money amount
    if "," in no_of_coins:
        no_of_coins = "".join(no_of_coins.split(","))

    # Calculate the difference between available money and item prices
    price_difference = [int(no_of_coins) - element_price for element_price in prices_of_items]

    # Find the index of the item with the smallest price difference
    index = smallest(price_difference)

    # Click the buy button for the item with the smallest price difference
    buy = driver.find_element(By.ID, list_of_items[index])
    buy.click()


# Set up Chrome options and create a new instance of the Chrome driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)

# Navigate to the target website
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Find the cookie element on the webpage
cookie = driver.find_element(By.ID, "cookie")

# List of IDs for the items that can be bought
add_on = ["buyCursor", "buyGrandma", "buyFactory", "buyMine", "buyShipment", "buyAlchemy lab", "buyPortal",
          "buyTime machine"]

# Get the prices of the items by parsing the text of their corresponding elements
add_on_prices = [(driver.find_element(By.ID, f"{items}")).text.split(" ")[
                     3 if (driver.find_element(By.ID, f"{items}")).text.split(" ")[2] == '-' else 2].split("\n")[0] for
                 items in add_on]

# Convert the item prices from strings to integers
price = [int(prices.replace(",", "")) if "," in prices else int(prices) for prices in add_on_prices]

# Set up a timeout for the script to run for 5 minutes
current = time.time()
timeout = current + (60 * 5)

# Schedule the checker function to run every 10 seconds
schedule.every(10).seconds.do(lambda: checker(add_on, price))

# Main loop to keep clicking the cookie and running the scheduled tasks until timeout
while time.time() < timeout:
    schedule.run_pending()
    cookie.click()

# Find and print the cookies per second (CPS) value from the webpage
per_second = driver.find_element(By.ID, "cps")
print(per_second.text)

# Quit the WebDriver session
driver.quit()
