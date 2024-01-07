#!/usr/bin/python3
"""implementing requests module to make web requests"""

if __name__ == '__main__':
    import requests

    res = requests.get('https://alx-intranet.hbtn.io/status')
    content = res.text
    content_type = type(content)
    print(f'Body response:\n'
          f'\t- type: {content_type}\n'
          f'\t- content: {content}')
