# from twitterScrapper import Bot
from snscrape.modules import twitter


# class ScrapTweet(Bot):
#   def __init__(self):
#     super.__init__()
#     self.runTwitter()
    

      



def get_tweets(keyword:str)->str:
  tweets = twitter.TwitterHashtagScraper(keyword).get_items()
  
  for tweet in tweets:
    print(tweet.content)
    
  return "Tweets Scraped Successfully"

def get_user_tweets(username:str)->str:
  tweets = twitter.TwitterUserScraper(username).get_items()
  
  for tweet in tweets:
    print(tweet.content)
    
  return "Tweets Scraped Successfully"



get_tweets("python")