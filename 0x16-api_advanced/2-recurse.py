#!/usr/bin/python3
"""Function that queries the Reddit API
and returns the number of subscribers"""


def recurse(subreddit, hot_list=[], after=None):
    """Function that queries the Reddit API
    and returns the number of subscribers"""
    import requests
    response = requests.get(f'https://www.reddit.com/r/{subreddit}/hot.json',
                            headers={'User-Agent': 'app/1.0'})
    if response.status_code == 200:
        for post in response.json()['data']['children']:
            hot_list.append(post['data']['title'])
        if response.json()['data']['after'] is not None:
            return recurse(subreddit, hot_list)
        else:
            return hot_list
    else:
        return None
