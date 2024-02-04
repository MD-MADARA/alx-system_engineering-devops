#!/usr/bin/python3
""" module doc """
import requests
import sys


def json_response(url, data=None):
    """get response using get request"""
    if data:
        if isinstance(requests.get(url).json(), list):
            return [result.get(data) for result in requests.get(url).json()]
        else:
            return requests.get(url).json().get(data)
    else:
        return requests.get(url).json()


def main():
    """main function"""

    url = "https://jsonplaceholder.typicode.com"
    EmployeeID = sys.argv[1]
    # urls:
    user_data = f"{url}/users/{EmployeeID}"
    user_tasks = f"{url}/todos?userId={EmployeeID}"
    completed_tasks = f"{user_tasks}&completed=true"

    # data:
    EMPLOYEE_NAME = json_response(user_data, "name")
    NUMBER_OF_DONE_TASKS = len(json_response(completed_tasks))
    TOTAL_NUMBER_OF_TASKS = len(json_response(user_tasks))

    # output
    print("Employee {} is done with tasks({}/{}):".format(
        EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS
    ))
    for task in json_response(completed_tasks):
        print(f"\t{task.get('title')}")


if __name__ == "__main__":
    main()
