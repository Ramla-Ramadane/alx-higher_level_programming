#!/usr/bin/python3
'''Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email
as a parameter, and displays the body of
the response (decoded in utf-8)'''


import urllib.request
import sys


if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1],
                                b'email=' + sys.argv[2].encode()) as req:
                                    print(req.read().decode('UTF-8'))
