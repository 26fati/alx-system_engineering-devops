#!/usr/bin/python3
"""fetches information from JSONplaceholder API and exports to CSV"""
import csv
import requests
import sys


if __name__ == '__main__':
    arg = sys.argv[1]
    todos_url = f"https://jsonplaceholder.typicode.com/users/{arg}/todos"
    user_url = f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"

    response1 = requests.get(user_url)
    response = requests.get(todos_url)
    user_data = response1.json()
    todos_data = response.json()

    username = user_data.get("username")
    rows = [[row.get('userId'), username,
             row.get('completed'), row.get('title')]
            for row in todos_data]
    with open(f'{arg}.csv', 'w') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(rows)
