#!/bin/bash
# takes in URL, sends a GET request with a header variable X-School-User-Id: 98
curl -sX GET -H "X-School-User-Id: 98" $1
