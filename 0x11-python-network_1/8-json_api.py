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
    if len(sys.argv) > 1:
        letter = sys.argv[1]
        r = requests.post("http://0.0.0.0:5000/search_user", {'q': letter})
        try:
            data = r.json()
            if len(data) == 0:
                print('No result')
            else:
                print("[{}] {}".format(data['id'], data['name']))
        except ValueError:
            print('Not a valid JSON')
    else:
        print("No result")
