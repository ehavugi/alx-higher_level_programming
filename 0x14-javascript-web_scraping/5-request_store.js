#!/usr/bin/node
// send a request and print out status code
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const fileName = process.argv[3];
request(url, function (error, response, body) {
  if (error) {
    console.error('error', error);
  }
  fs.writeFile(fileName, response.body, err => {
    if (err) {
      console.error(err);
    }
  });
});
