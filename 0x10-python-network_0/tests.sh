#!/usr/bin/bash
# Run all examples in the tasks
./0-body_size.sh 0.0.0.0:5000
./1-body.sh 0.0.0.0:5000/route_1 ; echo ""
./2-delete.sh 0.0.0.0:5000/route_3 ; echo ""
./3-methods.sh 0.0.0.0:5000/route_4.
./4-header.sh 0.0.0.0:5000/route_5 ; echo ""
./5-post_params.sh 0.0.0.0:5000/route_6 ; echo ""
./6-main.py
wc -l 6-peak.txt 
./100-status_code.sh 0.0.0.0:5000 ; echo ""
./100-status_code.sh 0.0.0.0:5000/nop ; echo ""
/101-post_json.sh 0.0.0.0:5000/route_json my_json_0 ; echo ""
./101-post_json.sh 0.0.0.0:5000/route_json my_json_1 ; echo ""
/101-post_json.sh 0.0.0.0:5000/route_json my_json_2 ; echo ""
./102-catch_me.sh ; echo ""
