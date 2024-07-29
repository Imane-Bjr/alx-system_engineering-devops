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
    name = response.get('name')
    response_to_dos = req.get(url_to_do).json()

    count = 0
    total = len(response_to_dos)
    for to_do in response_to_dos:
        if to_do.get('completed'):
            count += 1
    print("Employee {} is done with tasks({}/{}):".format(name, count, total))
    for to_do in response_to_dos:
        if to_do.get('completed'):
            print("\t {}".format(to_do['title']))
