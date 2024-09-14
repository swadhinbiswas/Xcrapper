import os
import sys
import time
class Settings:
  def get_driverpath():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(current_dir, 'chromedriver/chromedriver')
    return path



