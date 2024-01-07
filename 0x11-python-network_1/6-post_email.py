#!/usr/bin/python3
"""
Takes in url and an email address, sends post request
"""

if __name__ == '__main__':
  import requests
  import sys

  url = sys.argv[1]
  value = {'email': sys.argv[2]}
  res = requests.post(url, data=value)
  print(res.text)
