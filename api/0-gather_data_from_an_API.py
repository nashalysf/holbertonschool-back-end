#!/usr/bin/python3
"""
RESTFul API for employee
"""


import requests
import sys


if __name__ == "__main__":
    """ Gets employee todo information """
    id = sys.argv[1]
    TASK_TITLE = []
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0

user_url = request.get('https://jsonplaceholder.typicode.com/users/' + id)
EMPLOYEE_NAME = user_url.get('name')
todos = user_url.get('https://jsonplaceholder.typicode.com/todos/').json

for i in todos:
    if i.get('completed') is True:
        TASK_TITLE.append(i['title'])
        NUMBER_OF_DONE_TASKS += 1
    TOTAL_NUMBER_OF_TASKS += 1


print('Employee {} is done with tasks({:d}/{:d}):'.format(EMPLOYEE_NAME,
      NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

for j in TASK_TITLE:
    print("\t {}".format(j))
