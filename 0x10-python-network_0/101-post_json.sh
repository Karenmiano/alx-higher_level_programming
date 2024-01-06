#!/bin/bash
# takes URL and json file, sends POST request with the json data and displays response body
curl -sX POST -d "@$2" -H "Content-Type: application/json" "$1"
