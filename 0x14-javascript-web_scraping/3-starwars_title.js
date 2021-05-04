#!/usr/bin/node
const id = process.argv[2];
const request = require('request');
const swurl = 'https://swapi-api.hbtn.io/api/films/' + id;
request(swurl, function (error, response, body) {
  if (error) {
    console.error('error:', error);
  }
  const object = JSON.parse(body);
  console.log(object.title);
});
