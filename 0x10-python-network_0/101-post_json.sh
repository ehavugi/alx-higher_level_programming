#!/bin/bash
# use curl to get http code 
# Author: Emmanuel HAVUGIMANA
# Date : 2023
# For : ALX
curl --header "Content-Type: application/json" -X POST --data-raw "$(cat "$2")"  "$1"
