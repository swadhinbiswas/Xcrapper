# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.chrome.service import Service

# from selenium.webdriver.support import expected_conditions as EC
# import time 
# from bs4 import BeautifulSoup

# service=Service("/home/swadhin/Desktop/New folder/Twitter/cliapp/chromedriver/chromedriver")
# driver = webdriver.Chrome(service=service)  # Replace with your preferred browser
# driver.get("https://x.com/JamunaTV")  # Replace with the actual URL

# time.sleep(2)  # Allow 2 seconds for the web page to open
# scroll_pause_time = 1 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
# screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
# i = 1

# while True:
#     # scroll one screen height each time
#     driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
#     i += 3
#     soup=BeautifulSoup(driver.page_source,'html.parser')
#     mediaurl=set()
#     for img in soup.find_all('img'):
#            mediaurl.add(img.get('src'))
#     time.sleep(8)
#     # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
#     scroll_height = driver.execute_script("return document.body.scrollHeight;")  
#     # Break the loop when the height we need to scroll to is larger than the total scroll height
#     if (screen_height) * i > scroll_height:
#         break
    
# print(mediaurl)


import requests
from bs4 import BeautifulSoup
import asyncio


def get_image_urls(url:str)->set:
    response = requests.get(url)
    print(response.text)
    soup = BeautifulSoup(response.text, 'html.parser')
    mediaurl=[]

    for img in soup.find_all('img'):
        mediaurl.add(img.get('src'))
        print(img.get('src'))
    return mediaurl

url="https://x.com/ABhuttow"

x= get_image_urls(url)
print(x)
