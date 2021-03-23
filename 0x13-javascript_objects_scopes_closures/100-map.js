#!/usr/bin/node
const list1 = require('./100-data').list;

const map1 = list1.map((item, index, list1) => item * index);
console.log(list1);
console.log(map1);
