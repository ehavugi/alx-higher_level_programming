#!/bin/bash
# use curl to get http code  Author: Emmanuel HAVUGIMANA Date : 2023  For : ALX
curl --header "Content-Type: application/json" "$1" -X POST -d "$(cat "$2")"
