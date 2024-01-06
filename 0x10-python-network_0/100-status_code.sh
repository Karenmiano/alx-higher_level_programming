#!/bin/bash
# takes URL, sends request and displays status code
curl -s -o /dev/null -w "%{http_code}" "$1"
