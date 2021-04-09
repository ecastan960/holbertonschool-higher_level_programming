#!/bin/bash
# Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.
curl -s "$1" -I | grep -i 'HTTP/1.0' | cut -c 10-13
