#!/usr/bin/python3
"""
Takes in url, makes request and fetches value of X-Request-Id
from response headers
"""

import requests
import sys

if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    val = res.headers.get('X-Request-Id')
    print(val)
