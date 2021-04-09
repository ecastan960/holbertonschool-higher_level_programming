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
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], email)
    print(r.text)
