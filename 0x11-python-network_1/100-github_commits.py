#!/usr/bin/python3
# get 10 latest commits
import requests
import sys

commits = requests.get('https://api.github.com/repos/{}/{}/commits'.format(
          sys.argv[1], sys.argv[2]))
for i in commits.json()[:10]:
    print("{}: {}".format(i['sha'], i['commit']['author']['name']))
