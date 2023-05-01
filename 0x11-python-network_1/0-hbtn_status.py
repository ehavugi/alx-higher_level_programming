#!/usr/bin/python3
""" Fetch data """
import urllib.request
url = "https://alx-intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
    out = response.read()
    print("Body response:")
    print("    - type: {}".format(type(out)))
    print("    - content: {}".format(out))
    print("    - utf8 content: {}".format(out.decode('utf-8')))
