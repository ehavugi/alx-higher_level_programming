#!/usr/bin/python3
""" Send POST requests"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    with requests.post(url, data={"email": email}) as response:
        print(response.text)
