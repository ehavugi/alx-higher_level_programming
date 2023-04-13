#!/usr/bin/node
var fs = require("fs");
const argv = process.argv;

const fileA = String(argv[2]);
const fileB = String(argv[3]);
const fileC = String(argv[4]);
var data = {}
console.log(fileA, fileB, fileC);
const reader = function readingFile(filex, data) {
  fs.readFile(filex,"utf8", (err, buf) => {
    if (err) throw err;
      data =  buf.toString();
      console.log("buffer ", data);
  });
};

console.log(reader(fileA, data));
console.log("all data: ", data);
fs.writeFile(fileC, fileB, function(err) {
  if (err) throw err;
});

console.log("end");
