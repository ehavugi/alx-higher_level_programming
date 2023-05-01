#!/usr/bin/python3
""" Fetch data """
import urllib.request
url = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
    out = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(out)))
    print("\t- content: {}".format(out))
    print("\t- utf8 content: {}".format(out.decode('utf-8')))
