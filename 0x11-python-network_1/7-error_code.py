#!/usr/bin/python3
"""takes a url and prints body depending on status code"""

if __name__ == '__main__':
    import sys
    import requests

    response = requests.get(sys.argv[1])
    status_code = response.status_code
    if status_code >= 400:
        print(f'Error code: {status_code}')
    else:
        print(response.text)
