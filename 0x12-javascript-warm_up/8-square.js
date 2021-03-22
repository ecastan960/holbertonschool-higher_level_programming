#!/usr/bin/node
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else if (process.argv[2] > 0) {
  const times = process.argv[2];
  const text = 'x';
  for (let i = 0; i < times; i++) {
    console.log(text.repeat(times));
  }
}
