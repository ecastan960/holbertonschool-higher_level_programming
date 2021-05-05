#!/usr/bin/node
const url = process.argv[2];
const request = require('request');
const output = {};
let n = 0;
let count = 0;
let user = 1;
request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  const object = JSON.parse(body);
  while (object[n]) {
    while (object[n].userId === user) {
      if (object[n].completed === true) {
        count = count + 1;
      }
      n = n + 1;
      if (n === 200) {
        break;
      }
    }
    output['' + user] = count;
    user = user + 1;
    count = 0;
  }
  console.log(output);
});
