#!/usr/bin/python3
"""
queries the Reddit API and
prints the titles of the first 10 hot posts listed for a given subreddit
List the TOP 10 of popular in Reddit
"""


import requests as req
from sys import argv


def top_ten(subreddit):
    """Top Ten popular"""
    subreddit = argv[1]
    headers = {"User-Agent": "User_Agent_/3.0"}
    url = "https://api.reddit.com/r/{}/hot?limit=10".format(subreddit)

    response = req.get(url, allow_redirects=False, headers=headers)
    if response.status_code == 200:
        data = response.json()
        for query in data['data']['children']:
            print(query['data']['title'])
    else:
        print(None)
