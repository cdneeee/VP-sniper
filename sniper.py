from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time, sys, keyboard, threading
from webdriver_manager.chrome import ChromeDriverManager

# Set up Chrome options to specify the debugger address
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")

# Set up the driver to connect to the running Chrome instance
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# The URL we want to open
url = 'https://ru88.voynaplemyon.com/game.php?screen=overview_villages&intro'

# Open a new tab
driver.execute_script("window.open('');")

# Switch to the new tab
driver.switch_to.window(driver.window_handles[-1])

# Navigate to the URL
driver.get(url)

# Give the page some time to load
time.sleep(2)

def get_server_time():

    try:
        # Find the element by its ID
        server_time_element = driver.find_element(By.ID, 'serverTime')

        # Get the text from the element
        server_time_text = server_time_element.text

        # Print the time text
        print(f"Server time is: {server_time_text}")
    finally:
        # Close the browser
        time.sleep(5)
        sys.exit()
        
# Function to handle Alt key press
def on_alt_press(event):
    # Check if the pressed key is an Alt key (either left or right)
    if event.name == 'alt' or event.name == 'alt gr':
        print("Alt key pressed, getting server time...")
        time.sleep(1) # to avoid multiple presses
        # Run the Selenium part in a separate thread to not block the keyboard listener
        threading.Thread(target=get_server_time).start()

# Hook to listen for key press events
keyboard.hook(on_alt_press)

print("Press Alt key to get the server time from example.com. Press Ctrl+C to exit.")
keyboard.wait('ctrl+c')

#TODO make time fetch automated