#!/bin/bash
# use curl to get the body size
status=$(curl -L -s --head  -X DELETE "$1")
body_=$(curl -L -s -X DELETE  "$1")
check="200"
if [[ "$status" == *"$check"* ]]; then
	 echo -n "$body_"
fi
