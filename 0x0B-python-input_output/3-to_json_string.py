#!/usr/bin/python3
'''return JSON string'''
import json


def to_json_string(my_obj):
    '''function that returns the JSON representation of
    a string'''
    return json.dumps(my_obj)
