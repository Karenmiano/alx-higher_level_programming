#!/usr/bin/python3
"""Script that takes in url and sends request and finally
retrieves value of X-Request-Id variable in header response"""

if __name__ == "__main__":
    import urllib.request
    from sys import argv

    with urllib.request.urlopen(argv[1]) as response:
        val = response.getheader('X-Request-Id')
        print(val)
