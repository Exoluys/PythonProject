from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

# Set Chrome options to disable certain features and enable remote debugging
chrome_options = Options()
chrome_options.add_argument("--no-sandbox") # Bypass OS security model
chrome_options.add_argument("--disable-search-engine-choice-screen") # Disable search engine selection screen
chrome_options.add_argument("--remote-debugging-port=9222") # Allow remote debugging on port 9222
chrome_options.add_argument("--disable-gpu") # Disable GPU acceleration

# Specify the path to the ChromeDriver and initialize WebDriver
service = Service(executable_path="chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(options=chrome_options, service=service)

# Open the Google Form in the browser
driver.get('https://docs.google.com/forms/d/1bBKAGTK1KJJrVQBsm43e4zr5EuyHTc0Dwc2p8vZJuiY/edit')
driver.maximize_window() # Maximize browser window for better visibility
time.sleep(3) # Wait for 3 seconds to allow the page to load

# Fill out the "Name" field
name_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
name_field.send_keys('Jai Revankar')

# Fill out the "Email" field
email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
email_field.send_keys('jairevankar98@gmail.com')

# Select the "Gender" field
gender_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="i13"]/div[3]/div')))
gender_field.click()

# Fill out the "Date of Birth" field
dateOfBirth_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')))
dateOfBirth_field.send_keys('02022006')

# Fill out the "Phone Number" field
phoneNumber_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')))
phoneNumber_field.send_keys('+91 994956551')

# Click the "Submit" button
submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/div[2]')
driver.execute_script("arguments[0].click()", submit_button) # Execute a script to click the submit button

# Take a screenshot after submitting the form
driver.save_screenshot('screenshot.png')
time.sleep(2) # Pause for 2 seconds to ensure the form is submitted

# Quit the driver and close the browser
driver.quit()
