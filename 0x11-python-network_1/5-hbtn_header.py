#!/usr/bin/python3
""" Fetch data and retrieve X-Request-Id header"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with requests.get(url) as response:
        print(response.headers.get("X-Request-Id", None))
