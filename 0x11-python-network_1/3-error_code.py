#!/usr/bin/python3
"""takes in url, sends requests plus manages HTTPError exceptions"""

if __name__ == '__main__':
    import urllib.request
    import sys
    import urllib.error

    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: ", e.code)
