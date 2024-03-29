#!/usr/bin/python3
"""Display TODO list of a given employee using REST API"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    employee = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={
        "userId": sys.argv[1]}).json()
    completed = []
    for t in todos:
        if t.get("completed") is True:
            completed.append(t.get("title"))
    print("Employee {} is done with tasks({}/{}):".format(
        employee.get("name"), len(completed), len(todos)))
    for task in completed:
        print("\t {}".format(task))
