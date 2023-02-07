#!/usr/bin/python3
"""
Save json to a file

"""
import json


def save_to_json_file(my_obj, filename):
    """
    save to json file
    """
    with open(filename, "w", encoding='utf-8') as f:
        f.write(str(json.dumps(my_obj)))
