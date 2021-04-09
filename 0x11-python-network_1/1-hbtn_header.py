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
    with request.urlopen(sys.argv[1]) as response:
        html = response.read()
        header = response.info()
        print(header['X-Request-Id'])
