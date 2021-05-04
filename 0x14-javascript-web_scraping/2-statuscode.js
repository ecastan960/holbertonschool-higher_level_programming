#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
request(url, function (response) {
  console.log('statusCode:', response && response.statusCode);
});
