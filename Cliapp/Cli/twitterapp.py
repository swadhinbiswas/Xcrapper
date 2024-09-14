from style.style import TextStyle
from database.path import Settings
from style.style import TextStyle
import sys 
sys.path.append("..")
from app import App


class TwitterApp:
    def searchProfile(username:str, password:str)->str:
        pass
        
    
    def login():
        TextStyle().printtext("Login to Twitter")
        username = input(TextStyle().print_question("Enter your username: "))
        password = input(TextStyle().print_question("Enter your password: "))
        Settings.set_user(username,password)
        return username, password
    
    def logout():
        TextStyle().printtext("Do you want to Delete the User Credentials?")
        choice=input()
        if choice=="yes":
            Settings.delete_user()
        else:
            TextStyle().printtext("Logout from Twitter")
            print("\n.................................\n")
            TextStyle().printtext("You have successfully logged out from Twitter")
            print("\n.................................\n")
            App()
    
    def searchTweets(keyword:str)->str:
        pass
    def grabmediafromuser(username:str,password:str,link:str)->str:
        pass
        