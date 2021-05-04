#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
request(url, function (error, response, body) {
  console.error('error:', error);
  console.log('code:', response && response.statusCode);
});
