from requests import get
import os
from typing import List


class Downloader():
  def __init__(self,urls:List,username:str,len:int):
    self.urls=urls
    self.username=username
    self.count=len
    self.home_dir = os.path.expanduser('~/Downloads')
    self.imagepath=os.path.join(self.home_dir, f'{self.username}_{self.count}.jpg')
    
  def run(self):
    image = get(self.url)
    with open(self.imagepath, "wb") as file:
      file.write(image.content)
      self.count-=1
  



# import requests

# url="https://pbs.twimg.com/media/Fso4ZWJaAAAr7PW?format=jpg&name=360x360"
# image = requests.get(url)
# with open(f"{url.split('/')[-1]}.jpg", "wb") as file:
#     file.write(image.content)


