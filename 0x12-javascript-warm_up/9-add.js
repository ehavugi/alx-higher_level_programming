#!/usr/bin/node
const argv = process.argv;

console.log(add(Number.parseInt(argv[2]), Number.parseInt(argv[3])));

function add (a, b) {
  return a + b;
}
