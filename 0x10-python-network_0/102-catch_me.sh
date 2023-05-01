#!/bin/bash
# Get him, get the server to output a given tex CUrrently the redirects do continue to use PUT, they change to GET
curl  -v -X PUT  -d "user_id"="98" 0.0.0.0:5000/catch_me
