from Themes.style import TextStyle
from Database.path import Settings
from Cli.twitterapp import TwitterApp as Twitter
from Database.userinfo import User
from Functions.handelloop import handel_link




class App:
    def __init__(self):
        #Initialize the App and print the title and welcome message
        TextStyle().print_app_title()
        TextStyle().welcome()
        
        self.user=User()
        self.tw=Twitter()
        # await self.start_app()
        
    async def start_app(self):
        #Start the App
        
        TextStyle().choose_option()
        TextStyle().print_option("1","Login to Twitter")
        TextStyle().print_option("2","Logout from Twitter")
        TextStyle().print_option("3","Search Tweets")
        TextStyle().print_option("4","Search Profile")
        TextStyle().print_option("5","Grab Media from User")
        TextStyle().print_option("6","Exit")
        choice=input()
        if choice=="1":
            if self.user.check_user()==False:
                
                TextStyle().print_question("Enter your username: ")
                username = input()
                TextStyle().print_question("Enter your password: ")
                password = input()
                
                x= await self.tw.login(username,password)
                TextStyle().track_progress(range(15))
                TextStyle().print_success(x)
                await self.start_app()
            else:
                TextStyle().print_error("You are already logged in")
                self.start_app()
        elif choice=="2":
            await Twitter.logout()
        elif choice=="3":
            await Twitter.searchTweets()
        elif choice=="4":
           await Twitter.searchProfile()
        elif choice=="5":
           
            link=handel_link()
            data= await self.tw.grabmediafromuser(link)
            if data:
                TextStyle().print_info("Do you want to Save to Database or Local Storage(json)? yes/no")
                
                
                
            else:
                TextStyle().print_error("No Media Found")
                self.start_app()
            
                
            
            
            
            
            
            
            
            
            
            # TextStyle().print_info("Do you want to continue? yes/no")
            # choice=input().lower()
            # if choice=="yes":
            #     self.start_app()
            # else:
            #     self.user.closedb()
            #     TextStyle().print_info("Exiting...")
            #     TextStyle().print_info("Goodbye!")
            #     exit()
            
           
                
                
            
        elif choice=="6":
            self.user.closedb()
            TextStyle().print_info("Exiting...")
            TextStyle().print_info("Goodbye!")
            exit()
        else:
            TextStyle().print_error("Invalid Choice")
            self.start_app()
            
