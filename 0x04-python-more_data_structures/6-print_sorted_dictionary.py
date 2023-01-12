#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if not isinstance(a_dictionary, dict):
        return None
    keys = sorted(a_dictionary.keys())
    for key in keys:
        print("{}: {}".format(key, str(a_dictionary[key])))
