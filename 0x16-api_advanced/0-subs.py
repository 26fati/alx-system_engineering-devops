#!/usr/bin/pyrthon3
"""Function that queries the Reddit API
and returns the number of subscribers"""


def number_of_subscribers(subreddit):
    """Function that queries the Reddit
    API and returns the number of subscribers"""
    import requests
    response = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json',
                            headers={'User-Agent': 'app/1.0'})
    if response.status_code == 200:
        return response.json()['data']['subscribers']
    else:
        return 0
