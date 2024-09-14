import os
from typing import List
import re
import multiprocessing

from time import sleep

class Settings:
  
  def get_driverpath():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_dir, 'chromedriver/chromedriver')
    return path
  
  def get_userdatabase_dir():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_dir, 'user.txt')
    return path
  
  def set_user(usrname:str,password:str)->List:
    with open(Settings.get_userdatabase_dir(),'w') as f:
      f.write(f'{usrname}\n{password}')
      
  def downloadpath(user:str,format:str)->str:
    home_dir = os.path.expanduser('~/Downloads')
    file_path = os.path.join(home_dir, f'{user}.{format}')
    return file_path
  


data=["https://pbs.twimg.com/media/Fso4ZWJaAAAr7PW?format=jpg&name=360x360","https://pbs.twimg.com/media/FXdhe2VUsAEYcKg?format=jpg&name=240x240","https://pbs.twimg.com/media/FXdhe2VUsAEYcKg?format=jpg&name=240x240","https://pbs.twimg.com/media/FXdhe2VUsAEYcKg?format=jpg&name=240x240","https://pbs.twimg.com/media/FXdhe2VUsAEYcKg?format=jpg&name=240x240","https://pbs.twimg.com/media/FXdhe2VUsAEYcKg?format=jpg&name=240x240","https://pbs.twimg.com/media/FXdhe2VUsAEYcKg?format=jpg&name=240x240","https://pbs.twimg.com/media/FXdhe2VUsAEYcKg?format=jpg&name=240x240","https://pbs.twimg.com/media/FXdhe2VUsAEYcKg?format=jpg&name=240x240","https://pbs.twimg.com/media/FXdhe2VUsAEYcKg?format=jpg&name=240x240"]
class Download(multiprocessing.Process):
  def __init__(self,data):
    multiprocessing.Process.__init__(self)
    self.data=data
    
  def run(self):
    print(f"Downloading {self.data}")
    for i in self.data:
      os.system(f"wget {i}")
      sleep(2)
      print(f"Downloaded {i}")



# x=Settings.get_userdatabase_dir()
# print(x)
# print(Settings.get_driverpath())
# print(Settings.get_userdatabase_dir())

# print(Settings.define_downloadpath())
