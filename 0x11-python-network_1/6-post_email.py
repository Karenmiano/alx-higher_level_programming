#!/usr/bin/python3
"""
Takes in url and an email address, sends post request and displays body response
"""

if __name__ = '__main__':
    import requests
    import sys

    res = requests.post(argv[1], data={'email': argv[2]})
    print(res.text)