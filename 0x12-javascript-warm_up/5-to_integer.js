#!/usr/bin/node
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Not a number');
} else {
  console.log(`My number: ${Math.trunc(parseInt(process.argv[2]))}`);
}
