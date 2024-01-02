#!/usr/bin/python3
"""Python script to export data in the JSON format from all employees"""
import json
import requests
import sys


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)
    employees = response.json()

    dictionary = {}
    for employee in employees:
        employee_id = employee.get('id')
        employee_name = employee.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'
        .format(employee_id)
        url = url + '/todos/'
        response = requests.get(url)
        tasks = response.json()
        dictionary[employee_id] = []
        for task in tasks:
            dictionary[employee_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": employee_name
            })
    with open('todo_all_employees.json', 'w') as file:
        json.dump(dictionary, file)
