#!/usr/bin/node
// Read a text froma  file given as argument
const fs = require('fs');
const fileName = process.argv;

fs.readFile(fileName[2], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
