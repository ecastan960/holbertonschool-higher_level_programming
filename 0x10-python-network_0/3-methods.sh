#!/bin/bash
# Bash script that sends a DELETE request to the URL passed as the first argument and displays the body of the response
curl -s -X OPTIONS "$1" -i | grep -i 'Allow:' | cut -c 8-
