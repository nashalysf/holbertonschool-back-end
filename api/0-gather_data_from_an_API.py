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
    number_of_done_tasks = 0
    total_number_of_tasks = 0

    user_url = requests.get(
        'https://jsonplaceholder.typicode.com/users/' + id).json()
    employee_name = user_url.get('name')
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/users/" + id + "/todos").json()

    for task in todos:
        if task.get('userId') == int(id):
            if task.get('completed') is True:
                task_title.append(task['title'])
                number_of_done_tasks += 1
            total_number_of_tasks += 1

    print('Employee {} is done with tasks({:d}/{:d}):'.format(employee_name,
          number_of_done_tasks, total_number_of_tasks))

    for j in task_title:
        print("\t {}".format(j))
