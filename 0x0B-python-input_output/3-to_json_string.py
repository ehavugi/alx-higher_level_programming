#!/usr/bin/python3
"""
Module with json to string
"""
import json


def to_json_string(my_object):
    """
    get an object and jsonifies it
    """
    return json.dumps(my_object)
