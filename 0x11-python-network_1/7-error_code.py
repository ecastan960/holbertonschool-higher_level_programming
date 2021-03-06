#!/usr/bin/python3
""" Python script that takes in a URL,
sends a request to the URL and displays
the body of the response.
"""

import sys
import requests

if __name__ == "__main__":
    """Don't execute if imported
    """
    url = sys.argv[1]
    r = requests.get(sys.argv[1])
    if r.status_code < 400:
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))
