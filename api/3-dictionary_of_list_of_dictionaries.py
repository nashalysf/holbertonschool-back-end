#!/usr/bin/python3
"""
RESTFul API for employee
"""
import requests
import json

if __name__ == "__main__":
    """ Gets employee todo information """
    user_url = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()

    users_tasks = {}

    for user in user_url:
        tasks = requests.get(
            f"{user_url}/{user['id']}/todos").json()

    for user in user_url:
        user_id = user['id']
        username = user[username]
        users_tasks[user_id] = []
        for todo in tasks:
            if user_id == todo["userId"]:
                users_tasks[user_id].append({
                    "username": username,
                    "task": todo["title"],
                    "completed": todo["completed"]
                })

    with open('todo_all_employees.json', 'w') as f:
        json.dump(users_tasks, f)
