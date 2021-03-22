#!/usr/bin/node
const n = process.argv[2];

function factorial (n) {
  if (n <= 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
if (parseInt(n)) {
  console.log(factorial(n));
} else if (isNaN(n)) {
  console.log(1);
}
