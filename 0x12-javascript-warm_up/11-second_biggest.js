#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const numbers = process.argv.slice(2);
  numbers.sort(function (a, b) { return a - b; });
  console.log(parseInt(numbers[numbers.length - 2]));
}
