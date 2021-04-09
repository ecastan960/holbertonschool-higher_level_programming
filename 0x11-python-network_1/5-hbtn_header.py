#!/usr/bin/python3
"""Python script that takes in a URL, sends a request
to the URL and displays the value of the variable
X-Request-Id in the response header
"""

import sys
import requests

if __name__ == "__main__":
    """Don't execute if imported
    """
    r = requests.get(sys.argv[1])
    if 'X-Request-Id' in r.headers:
        print(r.headers['X-Request-Id'])
