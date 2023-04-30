#!/bin/bash
# use curl to get the body size
status=$(curl -L -s --head "$1")
body_=$(curl -L -s  "$1")
check="200"
if [[ "$status" == *"$check"* ]]; then
	 echo -n "$body_"
fi
