#!/bin/bash
# sends a delete request to URL passed and displays body of response
curl -s -X DELETE "$1"
