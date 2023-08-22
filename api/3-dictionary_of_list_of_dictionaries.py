#!/usr/bin/python3
"""
RESTFul API for employee
"""
import requests
import sys
import json

if __name__ == "__main__":
    """ Gets employee todo information """
    user_url = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()

    users_tasks = {}

    for user in user_url:
        tasks = requests.get(
            f"{user_url}/{user['id']}/todos").json()

    users_tasks[user['id']] = []
    for task in tasks:
        tasks_dict = {
            'username': user['username'],
            'task': task['title'],
            'completed': task['completed']
        }
        users_tasks[user['id']].append(tasks_dict)

    with open('todo_all_employees.json', 'w') as f:
        json.dump(users_tasks, f)
