#!/usr/bin/python3
"""
Returns the number of subscribers for a given subreddit
"""
from requests import get


def number_of_subscribers(subreddit):
   """ 
   Gets the number of subscribers
   """
   url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
   headers = {
      "User-Agent": "Ubuntu:v22.04LTS"
   }
   response = get(url, headers=headers, allow_redirects=False)
   if response.status_code == 404:
      return 0
   results = response.json().get("data")
   return results.get("subscribers") 

