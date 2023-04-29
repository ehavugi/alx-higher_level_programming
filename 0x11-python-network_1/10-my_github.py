#!/usr/bin/python3
""" Read user ID given authentication """
import sys
import requests
if __name__ == "__main__":
    r = requests.get('https://api.github.com/user',
                     auth=(sys.argv[1], sys.argv[2]))
    print(r.json().get("id"))
