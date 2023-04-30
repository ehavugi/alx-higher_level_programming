#!/bin/bash
# use curl to get the body size
status_=$(curl -s -L --head "$1")
body_=$(curl -s -L  "$1")
check="200 OK"
if [[ "$status_" == *"$check"* ]]; then
	 echo -n "$body_"
fi
