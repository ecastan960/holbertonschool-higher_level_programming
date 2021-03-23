#!/usr/bin/node
const list1 = require('./100-data').list;
const list2 = [];
console.log(list1);
for (let i = 0; i < list1.length; i++) {
  list2[i] = list1[i] * i;
}
console.log(list2);
