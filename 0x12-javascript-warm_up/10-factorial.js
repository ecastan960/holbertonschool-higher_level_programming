#!/usr/bin/node
const n = process.argv[2];
if (process.argv[2]) {
  function factorial (n) {
    if (n <= 1) {
      return 1;
    } else {
      return n * factorial(n - 1);
    }
  }
  console.log(factorial(n));
} else {
  console.log(1);
}
