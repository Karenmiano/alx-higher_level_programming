#!/bin/bash
# takes url and displays all HTTP methods server will accept
curl -isX OPTIONS "$1" | grep -oP "Allow: \K[A-Za-z, ]+"