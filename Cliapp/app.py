from style.style import TextStyle
from Cli.twitterapp import TwitterApp as Twitter
# from logintoTwitter import LoginToTwitter


class App:
    def __init__(self):
        #Initialize the App and print the title and welcome message
        TextStyle().print_app_title()
        TextStyle().welcome()
    
    

    def take_input(self):
        TextStyle().choose_option()
        choice = input()
        return choice

    def run(self):
        # Main logic of the App
        choice = self.take_input()
        if choice == "1":
            # Handle the "Login to Twitter" option
            username, password = Twitter.login()
        else:
            # Handle the "Continue without logging in" option
            Twitter.logout()
        
        
        
if __name__ == "__main__":
    App().run()
    


