#!/usr/bin/node
const a = process.argv[2];
const b = process.argv[3];
function add (a, b) {
  console.log(parseInt(a) + parseInt(b));
}

if (process.argv.length < 4) {
  console.log(NaN);
} else {
  add(a, b);
}
