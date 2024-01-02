#!/usr/bin/python3
"""
Uses the JSON placeholder api to query data about an employee
"""
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
    number = 0
    titles = ""
    for row in todos_data:
        if row.get("completed"):
            number += 1
            titles = titles + row.get('title') + "\n\t "
    print(f"Employee {user_data.get('name')} "
          f"is done with tasks({number}/{len(todos_data)}):")
    print(f"\t {titles}")
