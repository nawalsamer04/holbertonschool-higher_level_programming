#!/usr/bin/python3
"""
Task 2: Consuming and processing data from an API using Python (requests).

We use JSONPlaceholder (https://jsonplaceholder.typicode.com/posts)
to:
1) Fetch posts and print their titles.
2) Fetch posts and save selected fields to a CSV file.
"""

import csv
import requests


POSTS_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """
    Fetch all posts from JSONPlaceholder.
    - Print the HTTP status code
    - If successful (200), print the title of each post (one per line)
    """
    try:
        response = requests.get(POSTS_URL, timeout=10)
        print(f"Status Code: {response.status_code}")

        if response.status_code != 200:
            return

        posts = response.json()  # Convert JSON response to Python list of dicts
        for post in posts:
            print(post.get("title", ""))

    except requests.RequestException as exc:
        # Network issue, timeout, DNS error, etc.
        print("Status Code: 0")
        print(f"Request failed: {exc}")


def fetch_and_save_posts():
    """
    Fetch all posts from JSONPlaceholder.
    - If successful (200), write posts.csv containing columns: id, title, body
    """
    try:
        response = requests.get(POSTS_URL, timeout=10)

        if response.status_code != 200:
            return

        posts = response.json()

        # Keep only the required keys
        rows = [
            {"id": post.get("id"), "title": post.get("title"), "body": post.get("body")}
            for post in posts
        ]

        with open("posts.csv", mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(rows)

    except requests.RequestException:
        # If request fails, do nothing (or you could print an error—spec didn't require it)
        return
