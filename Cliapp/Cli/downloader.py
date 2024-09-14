from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup
from typing import List



service = Service('/home/swadhin/Desktop/New folder/Twitter/cliapp/chromedriver/chromedriver')
driver = webdriver.Chrome(service=service)
driver.get("https://x.com/JamunaTV")  # Replace with the actual URL


# Initialize a list to store the extracted URLs
urls = []

# Scroll down the page and extract URLs
while True:
    # Scroll to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    elems = driver.find_elements_by_xpath("//a[@href]")
    for elem in elems:
     print(elem.get_attribute("href"))
    

    

    # Wait for new content to load (adjust timeout as needed)
    # wait = WebDriverWait(driver, 10)
    # wait.until(EC.presence_of_element_located((By.CLASS_NAME, "css-9pa8cd")))  # Adjust CSS selector if needed

    # # Find and extract URLs (adjust CSS selector based on your target elements)
    # elements = driver.find_elements(By.CLASS_NAME, "css-9pa8cd")  # Find all anchor tags
    # for element in elements:
    #     href = element.get_attribute("src")
    #     if href and href not in urls:
    #         urls.append(href)

    # # Check if there are more elements to load
    # if len(elements) == 0:
    #     break

# Print the extracted URLs
print(urls)

# Close the browser
driver.quit()
# image_list = []
# x=0
# Image
# while True:
#     # Scroll to the bottom of the page
#     x=x+1
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#     # Wait for new images to load (adjust timeout as needed)
#     wait = WebDriverWait(driver, 10)
    
  

#     # Find and extract image URLs
#     images = driver.find_elements(By.CLASS_NAME, "css-9pa8cd")
#     for image in images:
#         image_url = image.get_attribute("src")
#         if image_url not in image_list:
#             image_list.append(image_url)

#     # Check if there are more images to load
#     # if len(images) == 0:
#     #     break
#     if x==10:

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException

# driver = webdriver.Chrome()  # Replace 'Chrome' with your desired browser
