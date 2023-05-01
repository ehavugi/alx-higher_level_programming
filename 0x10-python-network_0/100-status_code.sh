#!/bin/bash
# use curl to get http code 
# Author: Emmanuel HAVUGIMANA
# Date : 2023
# For : ALX
curl -s -o /dev/null -w "%{http_code}" "$1"
