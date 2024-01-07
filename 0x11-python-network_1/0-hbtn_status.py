#!/usr/bin/python3
"""Fetches content from link and displays type,
binary version and decoded version"""
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    ans = response.read()
response_type = type(ans)
decoded = ans.decode('utf-8')
print(f"Body response:\n"
      f"    -type: {response_type}\n"
      f"    -content: {ans}\n"
      f"    -utf8 content: {decoded}")
