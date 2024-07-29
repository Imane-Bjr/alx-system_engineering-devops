#!/usr/bin/python3
"""fetching user data using api"""


import requests as req
import sys

if __name__ == '__main__':
    ID_Employee = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(ID_Employee)
    url_to_do = "https://jsonplaceholder.typicode.com/users/{}/todos/".format(
        ID_Employee)
    response = req.get(url).json()
    username = response.get('username')
    response_to_dos = req.get(url_to_do).json()

    count = 0
    with open(f'{ID_Employee}.csv', 'w', encoding="utf-8") as file:
        for to_do in response_to_dos:
            status = to_do.get('completed')
            title = to_do.get('title')
            text = '"{}","{}","{}","{}"\n'.format(
                ID_Employee, username, status, title)
            file.write(text)
