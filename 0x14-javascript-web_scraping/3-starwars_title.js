#!/usr/bin/node
// send a request and print out status code
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
request(url + id, function (error, response, body) {
  if (error) {
    console.error('error', error);
  }
  console.log(JSON.parse(response.body).title);
});
