from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import requests
from PIL import Image
from io import BytesIO

# Set up Chrome options for headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Define the path to your WebDriver
driver_path = '/home/swadhin/Desktop/New folder/Twitter/chromedriver/chromedriver'

# Set up the Chrome driver
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

def get_image_urls(username):
    # Load the Twitter profile
    driver.get(f'https://twitter.com/{username}')
    
    
    time.sleep(2)
    
  
  
get_image_urls('swadhinbiswas')

