#!/usr/bin/node
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  const times = process.argv[2];
  const text = 'C is fun';
  for (let i = 0; i < times; i++) {
    console.log(text);
  }
}
