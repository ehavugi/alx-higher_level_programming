#!/usr/bin/node
const { argv } = require('node:process');

console.log(factorial(Number.parseInt(argv[2])));

function factorial (a) {
  if (Number.isInteger(a)) {
    if (a <= 0) { return 1; }
    return a * factorial(a - 1);
  }
  return 1;
}
