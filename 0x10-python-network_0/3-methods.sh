#!/bin/bash
# takes url and displays all HTTP methods server will accept
curl -sX OPTIONS "$1"
