#!/usr/bin/python3
"""
Takes in url and an email address, sends post request
"""

if __name__ = '__main__':
    import requests
    import sys

    url = sys.argv[1]
    email = {'email': argv[2]}
    res = requests.post(url, data=email)
    print(res.text)
