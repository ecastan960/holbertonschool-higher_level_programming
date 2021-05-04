#!/usr/bin/node
const url = process.argv[2];
const id = 18;
const request = require('request');
request(url, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  const object = JSON.parse(body);
  // const number = object.keys()
  let count = 0;
  let n = 0;
  let r = 0;
  const wedge = 'https://swapi-api.hbtn.io/api/people/' + id + '/';
  while (object.results[r]) {
    n = 0;
    while (object.results[r].characters[n]) {
      if (object.results[r].characters[n] === wedge) {
        count = count + 1;
      }
      n = n + 1;
    }
    r = r + 1;
  }

  console.log(count);
});
