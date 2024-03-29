#!/usr/bin/python3
'''Python script that fetches https://alx-intranet.hbtn.io/status'''


import urllib.request

url = 'https://alx-intranet.hbtn.io/status'


with urllib.request.urlopen(url) as response:
    html = response.read()
    type_html = type(html)
    print("Body response:")
    print("\t- type: {}".format(type_html))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode('utf-8')))
