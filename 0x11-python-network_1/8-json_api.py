#!/usr/bin/python3
""" Search API. form a post request and read output"""
import requests
import sys

if __name__ == "__main__":
    q = ""
    if len(sys.argv) >= 2:
        q = sys.argv[1]

    payload = {"q": q}
    url = "http://0.0.0.0:5000/search_user"
    with requests.post(url, data=payload) as response:
        try:
            json_res = response.json()
            if json_res:
                print("[{}] {}".format(json_res["id"], json_res["name"]))
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")
