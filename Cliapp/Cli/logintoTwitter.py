from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import asyncio
from bs4 import BeautifulSoup
from typing import List
from alive_progress import alive_bar


# class LoginToTwitter:
#     async def __init__(self, username, password):
#         self.username = username
#         self.password = password
        
# # Setup Chrome options
# chrome_options = Options()
# # chrome_options.add_argument("--headless")
# # chrome_options.add_argument("--no-sandbox")
# # chrome_options.add_argument("--disable-dev-shm-usage")
# chrome_options.add_argument("--start-maximized")

# # Replace 'path_to_chromedriver' with the actual path to your ChromeDriver
# service = Service('/home/swadhin/Desktop/New folder/Twitter/cliapp/chromedriver/chromedriver')
# driver = webdriver.Chrome(service=service, options=chrome_options)

# # Navigate to the login page




# driver.get('https://x.com/i/flow/login')

# # Wait for the page to load (Adjust the time if needed)
# time.sleep(10)

# # Locate the username/email/phone field
# username_field = driver.find_element(By.NAME, "text")
# username_field.send_keys('shawyanbiswas7268@gmail.com')  # Replace with your username or email

# # Click the 'Next' button
# next_button = driver.find_element(By.XPATH, '//span[text()="Next"]')
# next_button.click()

# # Wait for the password field to appear
# time.sleep(3)

# # Locate the password field
# password_field = driver.find_element(By.NAME, "password")
# password_field.send_keys('Fuckyou321@@@@')  # Replace with your password

# # Press Enter or click on the 'Log in' button
# password_field.send_keys(Keys.RETURN)

# # Wait for the login process to complete
# time.sleep(5)

# # Optionally, you can check if the login was successful by verifying the current URL or checking for specific elements
# if "home" in driver.current_url:
#     print("Login successful!")
# else:
#     print("Login failed!")



class Bot:
    def __init__(self,username,password):
        self.driverpath="/home/swadhin/Desktop/New folder/Twitter/Cliapp/chromedriver/chromedriver"
        self.chrome_options = Options()
        self.chrome_options.add_argument("--start-maximized")
        # self.chrome_options.add_argument("--headless")
        # self.chrome_options.add_argument("--no-sandbox") 
        # self.chrome_options.add_argument("--disable-dev-shm-usage")
        
        self.service=Service(self.driverpath)
        self.driver = webdriver.Chrome(service=self.service, options=self.chrome_options)
        self.loginurl="https://x.com/i/flow/login"
        self.username=username
        self.password=password
    async def runTwitter(self):
        self.driver.get(self.loginurl)
        self.login()
    async def login(self):
        time.sleep(10)
        username_field = self.driver.find_element(By.NAME, "text")
        username_field.send_keys(self.username)
        next_button = self.driver.find_element(By.XPATH, '//span[text()="Next"]')
        next_button.click()
        time.sleep(9)
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys(self.password)
        password_field.send_keys(Keys.RETURN)
        time.sleep(5)
        if "home" in self.driver.current_url:
            print("Login successful!")
           
        else:
            print("Login failed!")
        
        x=await self.get_user()
        print(x)
        
            
    async def get_user(self)->List:
        url="https://x.com/Yajnaseni25/media"
        self.driver.get(url)
        time.sleep(8)
        screen_hr = self.driver.execute_script("return window.screen.height;")
        i = 1
        all_media_urls=set()
        while True:
            self.driver.execute_script("window.scrollTo(0, {screen_hr}*{i});".format(screen_hr=screen_hr, i=i))
            i += 1
            print(i)
            
            
            
            links=await self.get_media_urls()
            for link in links:
                all_media_urls.add(link)
            time.sleep(2)
            scroll_height = self.driver.execute_script("return document.body.scrollHeight;")
            print(scroll_height)
         
                
            time.sleep(3)
            if (screen_hr) * i > scroll_height:
                break
        return all_media_urls
    
    async def get_media_urls(self)->set:
        
        media_urls=set()
        x=self.driver.find_element(By.XPATH, """//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/section/div""")
        x=x.get_attribute('innerHTML')
        soup=BeautifulSoup(x,'html.parser')
        for img in soup.find_all('img'):
            media_urls.add(img.get('src'))
        
        return media_urls


if __name__=="__main__":
    Bot("shawyanbiswas7268@gmail.com","Fuckyou321@@@@")