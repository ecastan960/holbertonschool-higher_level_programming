#!/usr/bin/node
const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

fs.readFile(fileA, (err, data) => {
  if (err) throw err;

  const file1 = data.toString();
  fs.appendFile(fileC, `${file1}\n`, (err) => {
    if (err) throw err;
  });
});

fs.readFile(fileB, (err, data) => {
  if (err) throw err;

  const file2 = data.toString();
  fs.appendFile(fileC, `${file2}`, (err) => {
    if (err) throw err;
  });
});
