#!/usr/bin/python3
"""
RESTFul API for employee
"""
import requests
import sys


if __name__ == "__main__":
    """ Gets employee todo information """
    id = sys.argv[1]
    task_title = []
    completed = 0
    total = 0

    user_url = request.get('https://jsonplaceholder.typicode.com/users/' + id
    name = user_url.get('name')
    todos = user_url.get('https://jsonplaceholder.typicode.com/todos/').json

    for i in todos:
        if i.get('completed') is True:
            task_title.append(i['title'])
            completed += 1
        total += 1


    print('Employee {} is done with tasks({:d}/{:d}):' \
            .format(name, completed, total
    for j in task_title:
        print("\t {}".format(j))
