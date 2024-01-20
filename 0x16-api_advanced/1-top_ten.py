#!/usr/bin/python3
"""
titles of 10 hot posts for a subreddit
"""
from requests import get


def top_ten(subreddit):
    """
    Titles of top 10 hot posts for a subreddit
    """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "Ubuntu:v22.04LTS"
    }
    params = {
        "limit": 10
    }
    response = get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]

