#!/bin/bash
# script that accepts a URL, sends a request to the URL and
# displays the size of the body of the response

if [[ -n $1 ]]
then
    content_length=$(curl -sI "$1" | grep -oP "^Content-Length: \K\d+")
    echo "$content_length"
fi
