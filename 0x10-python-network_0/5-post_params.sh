#!/bin/bash
# use curl to send a GET request with custom header variable
curl -s -X POST -d 'email=test@gmail.com' -d 'subject=I will always be here for PLD' "$1"
