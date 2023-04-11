#!/usr/bin/node
const { argv } = require('node:process');

if (Number.isInteger(Number.parseInt(argv[2]))) {
  for (let i = 0; i < Number.parseInt(argv[2]); i++) {
    console.log('C is fun');
}
} else { console.log('Missing number of occurrences'); }
