#!/usr/bin/node
const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

try {
  const data1 = fs.readFileSync(fileA, 'utf8');
  const data2 = fs.readFileSync(fileB, 'utf8');
  const text = `${data1}\n${data2}\n`;
  fs.writeFileSync(fileC, text);
} catch (err) {
  console.error(err);
}