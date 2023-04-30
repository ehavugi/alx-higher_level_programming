#!/bin/bash
# use curl to send a GET request with custom header variable
curl -s -H "X-School-User-Id: 98" "$1"
