#!/usr/bin/python3

def best_score(a_dictionary):
    _key = None
    if a_dictionary is None:
        return _key
    for key in a_dictionary.keys():
        if _key is None:
            _key = key
        if a_dictionary[_key] < a_dictionary[key]:
            _key = key
    return _key
