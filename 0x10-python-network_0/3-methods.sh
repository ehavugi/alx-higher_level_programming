#!/bin/bash
# use curl to request method OPTIONS that server support
curl -s  --head -X OPTIONS  "$1" | grep -o "Allow.*"|cut -c 8-
