#!/usr/bin/python3
"""Write a Python script that takes in a URL,
sends a request to the URL and displays the value of
the X-Request-Id variable found in the header of the response.
"""

import sys
from urllib import parse, request

if __name__ == "__main__":
    """Don't execute if imported
    """
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    data = parse.urlencode(email)
    data = data.encode('utf-8')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        html = response.read()
        print(html.decode('utf-8'))
