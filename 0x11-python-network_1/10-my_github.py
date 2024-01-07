#!/usr/bin/python3
"""takes  GITHUB credentials username and password and uses GITHubAPI
to display id"""

if __name__ == '__main__':
    import requests
    import sys

    url = f'https://api.github.com/user'
    response = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    json_decoded = response.json()
    print(json_decoded.get("id"))