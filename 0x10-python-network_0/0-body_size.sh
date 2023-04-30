#!/bin/bash
# use curl to get the body size
curl -sL "$1"|wc -c
