#!/usr/bin/python3
""" get 10 latest commits for a given user and repo"""
import requests
import sys
if __name__ == "__main__":
    response = requests.get('https://api.github.com/repos/{}/{}/commits'.
                            format(sys.argv[1], sys.argv[2]))
    commits = response.json()
    if len(commits) >= 10:
        for i in commits[:10]:
            print("{}: {}".format(i['sha'], i['commit']['author']['name']))
    else:
        for i in commits:
            print("{}: {}".format(i['sha'], i['commit']['author']['name']))
