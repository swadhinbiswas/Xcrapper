from Functions.linkverrify import verify_twitter_link
from  Themes.style import TextStyle

def handel_link()->str:
  
  
   while True:
      try:
        TextStyle().print_question("Enter the link of the user: ")
        input_link = input()
        if verify_twitter_link(input_link):
            TextStyle().print_success("Link Verified")
            TextStyle().print_info("Redirecting to the User Profile")
            break
        else:
            TextStyle().print_error("Invalid Link")
      except ValueError:
        TextStyle().print_error("Invalid Link")
        continue
   return input_link
 
 
 