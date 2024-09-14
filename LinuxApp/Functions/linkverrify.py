import requests

def verify_twitter_link(twitter_link):
    """Verifies if a given Twitter link is valid.

    Args:
        twitter_link: The Twitter link to verify.

    Returns:
        True if the link is valid, False otherwise.
    """

    try:
      response = requests.get(twitter_link)
      if response.status_code == 200:
            return True
      else:
            return False

    except requests.exceptions.RequestException:
        return False
