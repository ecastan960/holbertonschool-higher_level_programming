#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status
"""

import requests

if __name__ == "__main__":
    """Don't execute if imported
    """
    r = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
