#!/bin/bash
# takes url and displays all HTTP methods server will accept
curl -s -X OPTIONS "$1"
