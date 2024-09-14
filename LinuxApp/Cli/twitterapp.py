from Themes.style import TextStyle
from Database.path import Settings
from Cli import app
from Database.userinfo import User
from Functions.twitterScrapper import Bot
from typing import Optional
from Database.Dataframe import ScrapperFrame


"""
Swadhin Biswas @swadhinbiswas
web:https://swadhin.my.id
github:@swadhinbiswas

"""

class TwitterApp():

   def __init__(self):
       self.user=User()
    
    
        
    
   async def login(self,username:str,password:str)->str:
        self.user.set_user(username,password)
        return "User Logged in Successfully"
        
        
    
   async def logout(self):
        TextStyle().printtext("Do you want to Delete the User Credentials?")
        choice=input()
        if choice=="yes":
            self.user.delete_user()
            TextStyle().print_success("User Deleted Successfully")
            await app.App().start_app()
        else:
            await app.App().start_app()
    
   async def searchTweets(self,keyword:str,Limit:Optional[int]=None)->str:
        x=self.user.get_user()
        TextStyle().print_info("Searching Tweets")
        bot=Bot(x[0][0],x[0][1])
        bot.searchTweets(keyword,limit=Limit)

   async def grabmediafromuser(self,link:str)->str:
        x=self.user.get_user()
        TextStyle().print_info("Grabbing Media from User")
        bot=Bot(x[0][0],x[0][1])
        data= await bot.findallmedia(link)
        return data
        
        
       
   async def searchProfile(self,username:str,Limit:Optional[int]=None)->str:
        x=self.user.get_user()
        TextStyle().print_info("Searching Profile")
        bot=Bot(x[0][0],x[0][1])
        await bot.searchProfile(username,limit=Limit)

        return "Profile Searched Successfully"
    
    
        
