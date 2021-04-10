#!/usr/bin/python3
"""  Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to
display your id
"""

import sys
import requests

if __name__ == "__main__":
    """Don't execute if imported
    """
    username = sys.argv[1]
    password = sys.argv[2]
    r = requests.get("https://api.github.com/user", auth=(username, password))
    if r.status_code < 400:
        data = r.json()
        print(data['id'])
    else:
        print("None")
