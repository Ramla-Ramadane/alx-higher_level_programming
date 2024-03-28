#!/usr/bin/python3
''' Python script that takes in a URL and an email address,
sends a POST request tothe passed URL with the email as a
parameter, and finally displays the body of the response'''


import sys
import requests


if __name__ == '__main__':
    request = requests.post(sys.argv[1], {'email': sys.argv[2]})
    print(request.text)
