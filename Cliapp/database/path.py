import os
from typing import List

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
      



