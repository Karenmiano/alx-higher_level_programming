#!/bin/bash
# sends a delete request to URL passed and displays body of response

curl -sL -X DELETE "$1"
