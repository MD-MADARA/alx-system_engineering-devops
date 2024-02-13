#!/usr/bin/python3
"""
Module documentaion
"""
import requests

headers = {"User-Agent": "My Reddit Subscribers Checker"}


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit.
    """
    # URL for the subreddit API
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'My Reddit Subscribers Checker'}

    # Send GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the response is successful (status code 200)
    if response.status_code == 200:
        # Parse JSON response
        data = response.json()

        # Extract and print the titles of the first 10 hot posts
        # listed for a given subreddit.
        for post in data["data"]["children"]:
            print(post["data"]["title"])
    else:
        print("None")
