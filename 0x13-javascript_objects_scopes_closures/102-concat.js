#!/usr/bin/node
const fs = require('fs');

const fileA = process.argv[2];
const fileB = process.argv[3];
const fileC = process.argv[4];

const data1 = fs.readFileSync(fileA, 'utf8');
const data2 = fs.readFileSync(fileB, 'utf8');
fs.writeFileSync(fileC, data 1 + data 2, 'utf8');
