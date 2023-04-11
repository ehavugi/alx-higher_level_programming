#!/usr/bin/node
const argv = process.argv;

if (Number.isInteger(Number.parseInt(argv[2]))) {
  for (let i = 0; i < Number.parseInt(argv[2]); i++) {
    console.log(''.padStart(Number.parseInt(argv[2]), 'X'));
  }
} else { console.log('Missing size'); }
