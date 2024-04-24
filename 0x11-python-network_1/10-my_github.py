#!/usr/bin/python3
'''Python script that takes GitHub credentials'''


import requests
import sys


if __name__ == "__main__":
    search = requests.get(
        "https://api.github.com/user",
        auth=(sys.argv[1], sys.argv[2])
    )
    print(search.json().get("id"))
