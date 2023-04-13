#!/usr/bin/node
const fs = require('fs');
const argv = process.argv;

const fileA = String(argv[2]);
const fileB = String(argv[3]);
const fileC = String(argv[4]);
let data = {};
console.log(fileA, fileB, fileC);

fs.readFile(fileA, 'utf8', (err, buf) => {
  if (err) throw err;
  data = buf.toString();
  console.log('buffer ', data);
});

console.log('all data: ', data);
fs.writeFile(fileC, fileB, function (err) {
  if (err) throw err;
});

console.log('end');
