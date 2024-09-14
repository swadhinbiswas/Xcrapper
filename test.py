# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from bs4 import BeautifulSoup
# from selenium.webdriver.chrome.service import Service
# import time

# # Function to scroll and load tweets
# def scroll_down(driver, last_height):
#     # Scroll down to the bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
#     # Wait to load the page
#     time.sleep(2)
    
#     # Calculate new scroll height and compare with last scroll height
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     return new_height

# # Function to scrape tweets from a user's timeline
# def scrape_tweets(username):
#     url = f"https://x.com/{username}"
    
#     # Initialize Selenium WebDriver (e.g., using Chrome)
#     service=Service('/home/swadhin/Desktop/New folder/Twitter/cliapp/chromedriver/chromedriver')
#     driver = webdriver.Chrome(service=service)
#     driver.get(url)
    
#     time.sleep(2)  # Let the page load
    
#     # Scroll to the bottom of the page multiple times to load more tweets
#     last_height = driver.execute_script("return document.body.scrollHeight")
#     while True:
#         new_height = scroll_down(driver, last_height)
#         if new_height == last_height:
#             break
#         last_height = new_height
    
#     # Parse the page source with BeautifulSoup
#     soup = BeautifulSoup(driver.page_source, 'html.parser')
#     driver.quit()
    
#     # Find all tweet containers
#     tweets = soup.find_all('div', {'data-testid': 'tweet'})
    
#     tweet_texts = []
#     for tweet in tweets:
#         try:
#             tweet_text = tweet.find('div', {'lang': True}).get_text()
#             tweet_texts.append(tweet_text)
#         except AttributeError:
#             continue
#         print(tweet_texts)
#     return tweet_texts

# # Example usage
# username = "imsofiaijaz"  # Replace with the Twitter handle of the user whose tweets you want to scrape
# tweets = scrape_tweets(username)

# # Print each tweet
# for tweet in tweets:
#     print(tweet)

# # Optionally, save the tweets to a file
# with open(f"{username}_tweets.txt", "w", encoding="utf-8") as file:
#     for tweet in tweets:
#         file.write(tweet + "\n")


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from bs4 import BeautifulSoup

# service=Service('/home/swadhin/Desktop/New folder/Twitter/cliapp/chromedriver/chromedriver')
# driver = webdriver.Chrome(service=service)

# x=driver.get('https://x.com/Yajnaseni25/media')

# driver.implicitly_wait(10)
# x=driver.find_element(By.XPATH, """//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/section/div""")

# y=x.get_attribute('innerHTML')
# print(y)

# def get_html_under_class(driver, class_name):
#     """
#     Retrieves the HTML code within elements with the specified class name from the current web page.

#     Args:
#         driver: A Selenium WebDriver instance.
#         class_name: The name of the class to search for.

#     Returns:
#         A list of HTML strings representing the content within the elements.
#     """

#     html_content = driver.page_source
#     soup = BeautifulSoup(html_content, 'html.parser')
#     elements = soup.find_all('div', class_=class_name)  # Adjust tag name if needed

#     html_code = []
#     for element in elements:
#         html_code.append(str(element))

#     return html_code

# # Example usage:
#  # Replace with your preferred WebDriver
# driver.get('https://x.com/VertigoWarrior')  # Replace with the target URL

# class_name = 'my-class'  # Replace with the actual class name
# html_code = get_html_under_class(driver, "css-175oi2r")

# for code in html_code:
#     print(code)

# driver.quit()



# # def get_image_urls()->set:
    
# #     image_list =set()
# #     for image in image_element:
# #         image_src = image.get_attribute('src')
# #         image_list = [image_src]
# #     print(image_list)


# # get_image_urls()
    

# # driver.get('https://x.com/marjanahmed13')
# # # Find the image element using XPath
# # image_element = driver.find_element(By.CLASS_NAME, "css-9pa8cd")
# # # Get the image source URL
# # image_src = image_element.get_attribute('src')
# # # Store the image source in a list
# # image_list = [image_src]
# # print(image_list)

# css-175oi2r r-1wbh5a2 r-1habvwh r-16xksha
# css-175oi2r r-1wbh5a2 r-1habvwh r-16xksha
# css-9pa8cd


# from bs4 import BeautifulSoup

# def get_html_by_aria_label(html_content, aria_label):
#     """
#     Retrieves the HTML code within the element with the specified aria-label from the given HTML content.

#     Args:
#         html_content: The HTML content to parse.
#         aria_label: The value of the aria-label attribute to search for.

#     Returns:
#         The HTML string representing the content within the element, or None if not found.
#     """

#     soup = BeautifulSoup(html_content, 'html.parser')
#     element = soup.find('div', {'aria-label': aria_label})

#     if element:
#         return str(element)
#     else:
#         return None

# # Example usage:


# aria_label = 'MyDiv'
# html_code = get_html_by_aria_label(html_content, aria_label)

# if html_code:
#     print(html_code)
# else:
#     print("Element with aria-label not found.")



import tkinter as tk

# class MyApplication(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Frame Switching")
#         self.geometry("400x300")

#         self.frame1 = tk.Frame(self)
#         self.frame2 = tk.Frame(self)

#         self.label1 = tk.Label(self.frame1, text="This is Frame 1")
#         self.label1.pack(pady=20)

#         self.label2 = tk.Label(self.frame2, text="""This is Frame 2
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
#                                sdklsdlsdl;sjdljsdljs;dddddyrwyte
                               
                               
                        
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
                               
#                                wewewewe""")
#         self.label2.pack(pady=20)

#         self.button1 = tk.Button(self, text="Switch to Frame 1", command=self.show_frame1)
#         self.button1.pack(pady=10)

#         self.button2 = tk.Button(self, text="Switch to Frame 2", command=self.show_frame2)
#         self.button2.pack(pady=10)

#         self.show_frame1()

#     def show_frame1(self):
#         self.frame1.pack(fill="both", expand=True)
#         self.frame2.pack_forget()

#     def show_frame2(self):
#         self.frame2.pack(fill="both", expand=True)
#         self.frame1.pack_forget()

# if __name__ == "__main__":
#     app = MyApplication()
#     app.mainloop()

# import os

# # Define the universal path using $HOME
# home_dir = os.path.expanduser('~/Downloads')

# # Define your file path relative to the home directory
# file_path = os.path.join(home_dir, 'your_file_name.txt')

# # For example, saving the image URLs to a file
# image_urls_list = [
#     'https://pbs.twimg.com/media/Fso4ZWJaAAAr7PW?format=jpg&name=360x360',
#     'https://pbs.twimg.com/media/FXdhe2VUsAEYcKg?format=jpg&name=240x240',
#     # Add more URLs...
# ]

# # Save the list to a file in the home directory
# with open(file_path, 'w') as f:
#     for url in image_urls_list:
#         f.write(url + '\n')

# print(f'File saved to {file_path}')


listx=['https://pbs.twimg.com/media/Fso4ZWJaAAAr7PW?format=jpg&name=360x360','https://pbs.twimg.com/media/FXdhe2VUsAEYcKg?format=jpg&name=240x240', 'https://pbs.twimg.com/media/GE0QAzBa8AAppb2?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FhwIUncaAAE-gmE?format=jpg&name=360x360', 'https://pbs.twimg.com/media/F4xCUxnakAEHNMM?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GXbR5J2aIAAdCz1?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GCSlzOFbQAAZCuq?format=jpg&name=360x360', 'https://pbs.twimg.com/media/Fr_YyqrXoAE0MoL?format=jpg&name=360x360', 'https://pbs.twimg.com/media/F5z3_BCagAAfHNM?format=jpg&name=360x360', 'https://pbs.twimg.com/media/F_TBDJmaQAA5qYA?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FQ9Pf5wVkAI1ibX?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FfvLzo3aUAIaC1h?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GG_sd1_WkAAi5CI?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GCsltySasAAVKVM?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FQ33lKYVUAIgA01?format=jpg&name=360x360', 'https://pbs.twimg.com/media/F_midThb0AAzs1T?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GEbITzbaQAAMa-c?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FX4oYP8VQAAIiya?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FWmOEz4UYAAAs2E?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GQxrXh5agAAJ-1H?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GM4X_nMXEAEDziU?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FltHr_JaUAAnVPh?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FWhGnUmUsAAogu_?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GIzBWSdXgAAIzv2?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GKbyWd8aAAEimJ-?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FbLtC4eaIAEqToP?format=jpg&name=240x240', 'https://pbs.twimg.com/media/GMeDM5kbUAAH_EL?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FUv0YbNUEAAY6XC?format=jpg&name=360x360', 'https://pbs.twimg.com/media/F7Pu6cUaMAAj7v7?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FQyfz3UVEAAb4QA?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GRoUxmvbMAIgwhV?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FSYVLFvVgAAWe7f?format=jpg&name=360x360', 'https://pbs.twimg.com/ext_tw_video_thumb/1784834005717942272/pu/img/D4uOIEGx3TBZcwGJ?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GTTpOZqa8AAOoJy?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GFkK1A8aAAAwfIi?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FW6zjXfUEAAmm63?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GOprSUvaoAAAXTR?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GApj8fCb0AAOprQ?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FW_8lYiUEAA-10K?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GDTim6HboAAiGU-?format=jpg&name=360x360', 'https://pbs.twimg.com/media/F0qCqlRagAE2RWi?format=jpg&name=360x360', 'https://pbs.twimg.com/media/Fbq_XjTaQAE8DFO?format=jpg&name=360x360', 'https://pbs.twimg.com/media/F1N5NcjagAEUS_S?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FSI_qFGUUAEWQt0?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FqnOkm-WYAIgr1d?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FfUoAhJakAAVv5x?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FjIsoRIaEAI0v4j?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FWCOS2vUcAAMgVv?format=jpg&name=240x240', 'https://pbs.twimg.com/media/GRPWDVbasAAgsD2?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FXFJxCdUUAAcBZK?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GKFoGH3a8AAzalu?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FrUBsk8WIAEbboE?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GBHUKUgaQAACvaq?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FecUxmDaMAAMkLM?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FiFVvq3agAAHpWZ?format=jpg&name=240x240', 'https://pbs.twimg.com/media/F3YTeoPaQAArCj_?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FwZOj1MaQAEvqeZ?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FRb9uTYVIAIkHw2?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GB8ECMFakAA86ku?format=jpg&name=360x360', 'https://pbs.twimg.com/media/F76lBiVasAAAZ8A?format=jpg&name=360x360', 'https://pbs.twimg.com/media/F96SNbYa8AA8Kr3?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FdpL4SvagAA-pPs?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GM60MrCW4AAlElZ?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FxlamXOagAAsBgD?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GJxXcVybIAAKEKL?format=jpg&name=360x360', 'https://pbs.twimg.com/media/F62d0eYaQAApiCw?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FdeSfBZaAAApWH2?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GGncurpWMAAVdwX?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GKOSYdSbIAAhKGy?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FWrOmW3VsAAef4s?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GBb_OfUacAAVvqk?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FUBp1AHUAAAWQZP?format=jpg&name=360x360', 'https://pbs.twimg.com/media/Fa8dXm-VUAIFO0m?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FfLQ9SuaYAAcQU_?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GJCRN2SXsAA8qsz?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GGSKy1rW0AEByjH?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GAQf0C3bgAAXubc?format=jpg&name=360x360', 'https://pbs.twimg.com/media/F39h41uaEAAh4tU?format=jpg&name=360x360', 'https://pbs.twimg.com/media/F0C369baYAARgcr?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FWRpwOuVEAAqdDA?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FqDOwK1WYAIRouD?format=jpg&name=360x360', 'https://pbs.twimg.com/media/F5UnqxMa4AAHMmt?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GJ430YAbYAAfILi?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FSAUVQrUUAAw0xN?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GJMwBt1XEAAuzZw?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FctLiUKaUAEq1lt?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GJcbsBxW0AA8lGb?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GLvlV4xb0AA_ugW?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GC-0R4qb0AA3QPW?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FUqoRe2UsAAacic?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GUY_4MNasAAKHtz?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FW1xfS7UUAAEaK0?format=jpg&name=360x360', 'https://pbs.twimg.com/media/Fd9769haMAAO4D4?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GS52Ov0bIAYxRnI?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GPAIvNLbkAAOPJI?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GOQm5b8aIAI-WDY?format=jpg&name=360x360', 'https://pbs.twimg.com/media/F4gz0GtaAAAR319?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FoMxL5nWIAA9C8w?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GIefHqfWMAArizx?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FRM3wx8VsAAnpgl?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FSQIB51VIAEBCTd?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FQt6sAsUYAIl8nz?format=jpg&name=360x360', 'https://pbs.twimg.com/ext_tw_video_thumb/1732673667619024896/pu/img/M6rP5YKPLStKWDVJ?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FaN6TasVsAAHdXc?format=jpg&name=240x240', 'https://pbs.twimg.com/media/GLd97ciaoAAI3Qu?format=jpg&name=360x360', 'https://pbs.twimg.com/media/F2WtlzOaAAAF0YK?format=jpg&name=360x360', 'https://pbs.twimg.com/ext_tw_video_thumb/1733323419700371456/pu/img/7DOQPWIKNvJ418wW?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GJ7tfbebsAEfHKP?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FasmDOfVEAAzQFb?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FWW13LcUEAAfdJI?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FXXY68uVEAEBx--?format=jpg&name=240x240', 'https://pbs.twimg.com/media/F1yHhTgaQAAnZc_?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GRZwOCoa0AAmVRP?format=jpg&name=360x360', 'https://pbs.twimg.com/media/Fx_JG0taIAAAHiU?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FnjnXGcaAAAJW7V?format=jpg&name=360x360', 'https://pbs.twimg.com/media/F-vTs4YaAAALzPa?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FQ0fe_aVcAAE-TD?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GHhVYN2WMAA1xVr?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GK53PjKaoAAv9R3?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GDnklujbEAANrP1?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FxSqn0_aQAEjhYC?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GSdRFOUX0AA01wW?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FRCR4JoVgAE8FYN?format=jpg&name=360x360', 'https://pbs.twimg.com/media/F3pgxX6bEAA18Zo?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FlT2wX-WYAIPsTN?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FpP0QBmXoAUrLq0?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FmPPaFqaYAIJa_t?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FeSrB2YakAM9MUA?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GNduXuqXEAEGSRb?format=jpg&name=360x360', 'https://pbs.twimg.com/media/Ff0GnBYacAARyV5?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GWY2cGCXkAEpCHU?format=jpg&name=360x360', 'https://pbs.twimg.com/ext_tw_video_thumb/1521148944998227968/pu/img/XrteqSUD9vMFq3v_?format=jpg&name=small', 'https://pbs.twimg.com/media/Ff99myIaYAEi7hX?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FUQ1hkwUsAI0i53?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FrkGAWbWcAED-nO?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FgDsamsacAAhFCR?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FZkxJgyUYAAdLRk?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FUjf-Q4UAAEgI_x?format=jpg&name=360x360', 'https://pbs.twimg.com/media/Fh7EIQYaYAIcD9p?format=jpg&name=360x360', 'https://pbs.twimg.com/media/Fb_cEEaaQAENsIT?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FTtRqsKUEAAlK5X?format=jpg&name=360x360', 'https://pbs.twimg.com/media/F8d-bsmacAAtsL4?format=jpg&name=360x360', 'https://pbs.twimg.com/media/Fyd7BBLaIAIVbZS?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FS5fHQDVIAAOBxv?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FRtG2eZVsAARFo_?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FYhxw_UVEAAtVeV?format=jpg&name=360x360', 'https://pbs.twimg.com/media/Fogmjn2aQAA8kge?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FrLRvSVXwAIrjge?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GBW0pk3bQAAPFdk?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FTiiotwVUAIF6xU?format=jpg&name=360x360', 'https://pbs.twimg.com/media/Fv_ZY-saEAIyud2?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GBhGOJaaUAA3RB-?format=jpg&name=360x360', 'https://pbs.twimg.com/media/F9B6c4facAAGSko?format=jpg&name=240x240', 'https://pbs.twimg.com/media/FponR8nWIAIcyZ8?format=jpg&name=360x360', 'https://pbs.twimg.com/media/F6e_RkzaQAAbzvM?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FdKNm25aAAAYscT?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FijUQRZagAADymX?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FTLuSSSVsAAudS2?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GCcIX4dbcAAFTqi?format=jpg&name=360x360', 'https://pbs.twimg.com/media/Fy4psENakAE29is?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GXPugOmakAAcgbZ?format=jpg&name=360x360', 'https://pbs.twimg.com/media/F7f3CguagAA2uBU?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FX_kLLCUsAAqga9?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GPs8k_wbgAAvkOp?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FenFT8xaMAAruun?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FvSvVABagAI4Oc_?format=jpg&name=360x360', 'https://pbs.twimg.com/media/F5GTnDjaoAAwWPD?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GK0Xv2NaIAMbmii?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GQ45WCYaEAAvjaA?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GHW71dRXsAAcQW6?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FV39Nq4UUAAonmi?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GAAWkMYaAAAVd8z?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GSIz1gRaUAImJ55?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FlFhQ3zakAQHeQk?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FtW3peSakAAXxW2?format=jpg&name=360x360', 'https://pbs.twimg.com/media/Fdzpjp_akAALOpq?format=jpg&name=360x360', 'https://pbs.twimg.com/media/F-GB5J1akAAD_n-?format=jpg&name=360x360', 'https://pbs.twimg.com/media/Fgn9KusagAA9Jmr?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FfPYOnAakAE7pkz?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GEQSvsXbsAEwKbw?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FV83iFIUEAAJImV?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GA9H0c4bgAAV6mj?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GBMdDJbaQAAvXnV?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GGCkTcmWsAAz64m?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GLR49RXawAAvgzO?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FoXIgaRagAAg10a?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FZTKHxuVUAA9tte?format=jpg&name=360x360', 'https://pbs.twimg.com/ext_tw_video_thumb/1592179464045481987/pu/img/T_UJPd2l7fRuW6GU?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GFZbc_QbMAAVJTu?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FfbcrfhaAAAf39S?format=jpg&name=360x360', 'https://pbs.twimg.com/media/F3E8LRKaYAAJyCA?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GVpMOIPWsAAC4gI?format=jpg&name=360x360', 'https://pbs.twimg.com/media/F6PY1OZaIAAoUWY?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FliQPkQagAgeUOm?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FRn7x8jVUAAzAoN?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FRTXfX9VsAAa1wS?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FfA6P2sacAA58Q7?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FY7r_O0VsAEd8bv?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FWLdRqbVEAIdtSh?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FRIPI0TVUAEZhkH?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GBR0mGOa4AAwt__?format=jpg&name=360x360', 'https://pbs.twimg.com/media/F9qARQBagAA2K9u?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FwpftMSagAAV2XN?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FexaCe1agAAaHD6?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FVtq8gGUUAAEj6b?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FRJEJ1XVEAA4WFY?format=jpg&name=240x240', 'https://pbs.twimg.com/media/FZu6eAGVQAANy96?format=jpg&name=360x360', 'https://pbs.twimg.com/media/Fs4KrWtaIAACBw1?format=jpg&name=240x240', 'https://pbs.twimg.com/media/Fu3xXA1akAIAvqO?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FfjucCKaEAIzryM?format=jpg&name=360x360', 'https://pbs.twimg.com/media/F_CtQu-bMAAtxwq?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GTHG-R2bcAAtFCn?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FhBUH_TakAENPKw?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GCGM4ryakAAueiq?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FeG7CNNaMAA391N?format=jpg&name=360x360', 'https://pbs.twimg.com/media/F59Vpt6awAAohnV?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GQWGBpXakAACD_W?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GEGbbzfbEAA7k41?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GDNg3KObwAAyp0s?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FYatJdhVUAAvsZl?format=jpg&name=240x240', 'https://pbs.twimg.com/media/FU_W3XRUEAAIN6E?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FR7j4LlVkAAZCyb?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FvFym64aIAAQdUO?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FVhKnYVUEAImf0J?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GBsr08caEAAWvdr?format=jpg&name=360x360', 'https://pbs.twimg.com/media/Fm5dkbdaUAApsKa?format=jpg&name=360x360', 'https://pbs.twimg.com/media/F4MXzhUakAARPBS?format=jpg&name=360x360', 'https://pbs.twimg.com/media/Fos_wPMaAAAO_fc?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GDdvdNSa0AABbTE?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FbWIC2EagAAJcEy?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FadvM5DVQAAd0yV?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FZ-eHijUIAAUsaO?format=jpg&name=360x360', 'https://pbs.twimg.com/media/Fl9SCy9aUAA2P_E?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FgdrAGmacAATRL9?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FgAPnuJVsAAoUeG?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GVeS7npXMAA-EoK?format=jpg&name=360x360', 'https://pbs.twimg.com/media/Fn5YfzfagAAZQRZ?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GPaT8eHaEAE_QaY?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FYNKPLGUcAEnwAv?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FSrfwDFVsAAbyz5?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GAzsPO9akAAhvBu?format=jpg&name=360x360', 'https://pbs.twimg.com/media/Fo1F_LPaMAEdVKN?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FXkPrSnUcAAxTPM?format=jpg&name=240x240', 'https://pbs.twimg.com/media/FejIjoTaYAAMVGU?format=jpg&name=240x240', 'https://pbs.twimg.com/media/FTDrrBzVEAANq24?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FzR8bSJakAEhjer?format=jpg&name=360x360', 'https://pbs.twimg.com/media/F-jkCFyaAAANrFL?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GMBi-1WbAAArBFH?format=jpg&name=360x360', 'https://pbs.twimg.com/media/F-VQogDbMAAevCF?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FT8jP7zUEAAO1Xf?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FhWaPAnaUAExrLE?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FjXy9BdaEAE6MMp?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GWFcxccasAAbhNP?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GFD8L9EboAAHLBL?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GB_-o3gbQAAQiRd?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FmbhIvkaMAA47c7?format=jpg&name=360x360', 'https://pbs.twimg.com/media/Fjno8QtagAAgIfc?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GD9nvHwakAA39Dc?format=jpg&name=360x360', 'https://pbs.twimg.com/media/Fe7pQfsaUAI1FNz?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FkJpercakAAcqLL?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FzrUYFHagAAB6S1?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FdkTqxraAAAaM8o?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GDz63m3b0AAoUFE?format=jpg&name=360x360', 'https://pbs.twimg.com/ext_tw_video_thumb/1766319453640245248/pu/img/2x0O5oyGDNa6RxP5?format=jpg&name=360x360', 'https://pbs.twimg.com/media/Fj8PhLjaMAEIrwu?format=jpg&name=360x360', 'https://pbs.twimg.com/media/Fgz2yjNaEAAIRS8?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GCkS2s4agAAqsT_?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FXrITy0UUAI6Kr4?format=jpg&name=360x360', 'https://pbs.twimg.com/media/F20aKO2aoAAgXta?format=jpg&name=360x360', 'https://pbs.twimg.com/media/F1a0OAvaMAEImQO?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FVOyZCLUYAElQ2m?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FQvV4skVcAAFRbz?format=jpg&name=360x360', 'https://pbs.twimg.com/media/Fw8xWCKakAAPVKn?format=jpg&name=360x360', 'https://pbs.twimg.com/ext_tw_video_thumb/1734030730139926528/pu/img/3xu4JbXR3QxJi9oN?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FYDCGAgUYAIBLDm?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GHAoxyTXcAEA1U8?format=jpg&name=360x360', 'https://pbs.twimg.com/ext_tw_video_thumb/1519347300048416768/pu/img/c-BAA6A4t3F_ng2O?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FVyuroIUcAE4GTc?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GVPsD1sa4AAYVRk?format=jpg&name=360x360', 'https://pbs.twimg.com/media/F2nU8XNbYAE27tR?format=jpg&name=360x360', 'https://pbs.twimg.com/media/Fcgd2XYacAE2te3?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FYsTcAaaQAALE7c?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GNrhbNGbsAAGOp5?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GTlgYoYaQAAzTBI?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GUhaHXkagAA_kZY?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GU6MUkCa4AMId23?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FgTgZZ_acAAB81q?format=jpg&name=360x360', 'https://pbs.twimg.com/media/F5kHRWyaEAAnkBv?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FTQ39uOVEAAW8-H?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FWb_6K3UIAAYJmf?format=jpg&name=360x360', 'https://pbs.twimg.com/media/Fkk8rg0agAEm8GU?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FrzpyTZXsAEH1O0?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FTa6nvWUcAIWOuK?format=jpg&name=360x360', 'https://pbs.twimg.com/media/Fc9SiCwakAEAhbc?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FVmYjM1VIAAbzVZ?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GJqjjyMW4AAgICt?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FWGLAtlVEAAgFl1?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FiQaNSbaAAArMl5?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FRhTAI7UcAAfMeq?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GKkaSVpagAAk9T_?format=jpg&name=360x360', 'https://pbs.twimg.com/media/F9VvzBpaQAEAzy0?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FROOjbiVcAAPeyy?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FhNFM29acAEeEXP?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FuA2LORaUAUJyJk?format=jpg&name=360x360', 'https://pbs.twimg.com/media/Fi0jH4QacAYmOPO?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GLI3mj0aUAAbLuq?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FehPnCCagAAPfcM?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FSvTPWgVEAEuO4P?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GN2CZ-caoAANT-M?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GBxK8G8bQAA9ZoT?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GH-TyB-WMAAoe9c?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FhlyRksaAAAjmV4?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GC0JENpa8AApiqA?format=jpg&name=360x360', 'https://pbs.twimg.com/media/FcToQBXagAIqiFK?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GAeeODbb0AAwmYa?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GP97DUWaQAASSGX?format=jpg&name=360x360', 'https://pbs.twimg.com/media/GVzjZKSWIAE0XOQ?format=jpg&name=360x360']




import re

def extract_string_after_media(url):


  match = re.search(r"media\/(.*?)\?", url)
  if match:
    return match.group(1)
  else:
    return None
ids=[]
# Example usage:
for url in listx:
    result = extract_string_after_media(url)
    ids.append(result)

import pprint

jsonformat = {"user": ids}


