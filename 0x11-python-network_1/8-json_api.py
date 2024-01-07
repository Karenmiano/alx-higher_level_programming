#!/usr/bin/python3
"""takes in letter, makes request to url and anticipates json data"""

if __name__ == '__main__':
    import requests
    import sys

    letter = "" if len(sys.argv) != 2 else sys.argv[1]
    value = {'q': letter}
    url = 'http://0.0.0.0:5000/search_user'
    try:
        res = requests.post(url, data=value)
        json_decoded = res.json()
        if len(json_decoded) == 0:
            print("No result")
        else:
            id = json_decoded.get('id')
            name = json_decoded.get('name')
            print(f'[{id}] {name}')
    except json.decoder.JSONDecodeError:
        print("Not a valid JSON")
