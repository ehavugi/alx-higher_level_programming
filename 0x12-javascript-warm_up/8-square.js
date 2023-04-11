#!/usr/bin/node
const argv = process.argv;

if (Number.parseInt(argv[2]) > 0) {
  for (let i = 0; i < Number.parseInt(argv[2]); i++) {
    console.log(''.padStart(Number.parseInt(argv[2]), 'x'));
  }
} else { console.log('Missing size'); }
