#!/bin/bash
# Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl 127.0.0.1:5000 -sI | grep -i 'content-length:' | cut -d ' ' -f2
