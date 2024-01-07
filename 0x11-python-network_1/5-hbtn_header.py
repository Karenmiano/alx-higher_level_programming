#!/usr/bin/python3
"""Takes in url, makes request and fetches value of X-Request-Id
from response headers"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)
    val = res.headers.get('X-Request-Id')
    print(val)
