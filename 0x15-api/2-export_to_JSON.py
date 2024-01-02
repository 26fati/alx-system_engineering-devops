#!/usr/bin/python3
"""fetches information from JSONplaceholder API and exports to CSV"""
import json
import requests
import sys


if __name__ == '__main__':
    arg = sys.argv[1]
    todos_url = f"https://jsonplaceholder.typicode.com/users/{arg}/todos"
    user_url = f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"

    response1 = requests.get(user_url)
    response = requests.get(todos_url)
    if response.status_code == 200 and response1.status_code == 200:
        user_data = response1.json()
        todos_data = response.json()
        username = user_data.get("username")
        rows = [{"task": row.get('title'), "completed": row.get('completed'),
                 "username": username} for row in todos_data]
        dic = {arg: rows}
        with open(f"{arg}.json", "w") as file:
            json.dump(dic, file)
