#!/usr/bin/python3
"""Export todo list of an employee to a csv file"""
import csv
import requests
import sys


if __name__ == "__main__":
    employee_number = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    employee = requests.get(url + "users/{}".format(employee_number)).json()
    employee_name = employee.get("username")
    todos = requests.get(url + "todos", params={
        "userId": employee_number}).json()
    with open('{}.csv'.format(employee_number), 'w', newline="") as file:
        for t in todos:
            file.write('"{}","{}","{}","{}"\n'
                       .format(employee_number, employee_name,
                               t.get('completed'), t.get('title')))
