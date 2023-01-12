#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    if not isinstance(a_dictionary, dict):
        return None
    keys = set(a_dictionary.keys())
    for key in keys:
        if a_dictionary[key] == value:
            a_dictionary.pop(key)
    return a_dictionary
