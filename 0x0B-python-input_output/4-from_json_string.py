#!/usr/bin/python3

"""
to from json to obj
"""
import json


def from_json_string(my_str):
    """
    return object.
    """
    return json.load(my_str)
