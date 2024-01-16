#!/usr/bin/python3
"""Function that queries the Reddit API
and prints the titles of the first 10 hot posts listed for a given subreddit"""


def top_ten(subreddit):
    """Function that queries the Reddit API
    and prints the titles of the first 10 hot
    posts listed for a given subreddit"""
    import requests
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(url, headers={'User-Agent': 'app/1.0'})
    if response.status_code == 200:
        for post in response.json()['data']['children']:
            print(post['data']['title'])
    else:
        print(None)
