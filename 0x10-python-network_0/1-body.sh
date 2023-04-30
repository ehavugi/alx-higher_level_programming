#!/bin/bash
# use curl to get the body content
status_=$(curl -s --head "$1")
body_=$(curl -s  "$1")
check="200 OK"
if [[ "$status_" == *"$check"* ]]; then
	 echo -n "$body_"
fi
