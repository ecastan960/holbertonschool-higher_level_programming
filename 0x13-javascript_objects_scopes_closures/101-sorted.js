#!/usr/bin/node
const data = require('./101-data').dict;
const newDict = {};
for (const key in data) {
  newDict[data[key]] = key;
}
console.log(newDict);
