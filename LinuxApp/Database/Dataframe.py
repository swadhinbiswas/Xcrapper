import pandas as pd
from typing import Optional
import re

class ScrapperFrame:
  def __init__(self,data,user:str):
    self.data=data
    self.user=user
  
  def extracturl(self,url:str)->str:
    match = re.search(r'media\/(.*?)\?', url)
    if match:
      return match.group(1)
    else:
      return None
    
  def convert_to_json(self):
    data=list(self.data)
   
    list1=[]
    for i in data:
      id=self.extracturl(i)
      list1.append(id)
    print(list1.__len__())
 
    jsondata={f"{self.user}":list1}
    return jsondata
