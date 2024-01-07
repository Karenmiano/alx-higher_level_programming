#!/usr/bin/python3
"""Takes in url and email, sends POST request with email as parameter
finally displays body of response"""

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    param = urllib.parse.urlencode({'email': sys.argv[2]})
    param = param.encode('utf-8')
    with urllib.request.urlopen(sys.argv[1], param) as response:
        page = response.read().decode('utf-8')
        print(page)
