#!/bin/bash
# Get him, get the server to output a given text
# CUrrently the redirects do continue to use PUT, they change to GET
curl  -v -X PUT  -d "user_id"="98" 0.0.0.0:5000/catch_me
curl -v -X PUT -d "user_id"="98" 0.0.0.0:5000/catch_me_2
curl -v -H "X-School-User-Id: 98" -X PUT -d "user_id"="98" 0.0.0.0:5000/catch_me_3
echo 
