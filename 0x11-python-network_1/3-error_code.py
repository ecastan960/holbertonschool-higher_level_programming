#!/usr/bin/python3
"""Write a Python script that takes in a URL,
sends a request to the URL and displays the value of
the X-Request-Id variable found in the header of the response.
"""

import sys
from urllib import parse, request, error

if __name__ == "__main__":
    """Don't execute if imported
    """
    url = sys.argv[1]
    req = request.Request(url)
    try:
        with request.urlopen(req) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except error.HTTPError as e:
        code = e.code
        print('Error code: {}'.format(code))
