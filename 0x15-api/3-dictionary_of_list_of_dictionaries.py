#!/usr/bin/python3
"""fetches information from JSONplaceholder API and exports to CSV"""
import json
import requests


if __name__ == '__main__':
    users_url = f"https://jsonplaceholder.typicode.com/users"

    response1 = requests.get(users_url)
    users_data = response1.json()
    dic = {}
    for row in users_data:
        id = row.get('id')
        todos_url = f"https://jsonplaceholder.typicode.com/users/{id}/todos"
        response = requests.get(todos_url)
        todos_data = response.json()
        username = row.get("username")
        rows = [{"username": username, "task": row.get('title'),
                 "completed": row.get('completed')} for row in todos_data]
        dic[row.get('id')] = rows
    with open("todo_all_employees.json", "w") as file:
        json.dump(dic, file)
