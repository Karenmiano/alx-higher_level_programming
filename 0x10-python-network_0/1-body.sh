#!/bin/bash
# receives url, sends GET request and displays bodu of response only if status code is 200 OK
curl -s -o save -X GET -w "%{http_code}" "$1" | grep -q "200" && sudo cat save