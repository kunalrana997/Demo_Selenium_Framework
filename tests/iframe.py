from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up your WebDriver (for example, using Chrome)
driver = webdriver.Chrome()

# Open the page
driver.get('https://suniljindal.com/')  # Replace with the actual URL containing the Trello board
original_window = driver.current_window_handle
print("original_window", original_window)
# Wait for the iframe to be available and switch to it
wait = WebDriverWait(driver, 10)
iframe = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "trello-board")))

# Switch to the iframe
driver.switch_to.frame(iframe)

# Now locate and click on the board element (assuming it has a class 'board-name' or similar)
board_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"div#board-container trello-board-tile")))

board_element.click()  # Click the board element
driver.switch_to.default_content()
# Wait for the new tab to open
time.sleep(5)  # Adjust the sleep time as needed; using explicit waits is preferred.

# Get the current window handles
# original_window = driver.current_window_handle
print("driver.window_handles", driver.window_handles)
new_window = [window for window in driver.window_handles if window != original_window][0]

# Switch to the new tab
driver.switch_to.window(new_window)

# Check if the URL contains 'trello.com'
if 'trello.com' in driver.current_url:
    print("Successfully navigated to Trello:", driver.current_url)
else:
    print("Failed to navigate to Trello. Current URL:", driver.current_url)

# Optionally, switch back to the original tab
driver.switch_to.window(original_window)

# Close the new tab if you want
driver.close()

# Close the original browser window
driver.quit()
