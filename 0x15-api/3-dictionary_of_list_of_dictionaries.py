#!/usr/bin/python3
"""returns all the informations for the employees"""

import json
import requests as req
if __name__ == '__main__':
    id = 1
    result = {}
    while True:
        url = "https://jsonplaceholder.typicode.com/"
        users = "users?id={}".format(id)
        todos = "todos?userId={}".format(id)
        user = req.get(f"{url}{users}").json()
        if not user:
            break

        username = user[0].get("username")
        Todos = req.get(("{}{}".format(url, todos))).json()

        result[id] = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in Todos
        ]
        id += 1

    with open("todo_all_employees.json", "w") as file:
        json.dump(result, file)
