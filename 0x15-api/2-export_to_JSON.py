#!/usr/bin/python3
"""Export todo list of an employee to a csv file"""
import json
import requests
import sys


if __name__ == "__main__":
    employee_number = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    employee = requests.get(url + "users/{}".format(employee_number)).json()
    employee_name = employee.get("username")
    todos = requests.get(url + "todos", params={
        "userId": employee_number}).json()

    with open("{}.json".format(employee_number), "w") as jsonfile:
        json.dump({employee_number: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": employee_name
            } for t in todos]}, jsonfile)
