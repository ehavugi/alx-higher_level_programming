#!/usr/bin/python3

"""
create obj from file
"""
import json


def load_from_json_file(filename):
    """
    load json from file name.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return (json.load(f))
