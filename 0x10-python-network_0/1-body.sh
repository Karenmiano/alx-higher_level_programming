#!/bin/bash
# receives url, sends GET request and displays bodu of response only if status code is 200 OK
curl -sL "$1"
