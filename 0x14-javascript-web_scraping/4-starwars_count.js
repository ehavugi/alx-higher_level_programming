#!/usr/bin/node
// get star wars films and check number of films that
// edge Antilles, character ID 18  is in and return
// the numbers to console
const request = require('request');
const url = process.argv[2];
request(url, function (error, response, body) {
  if (error) {
    console.error('error', error);
  }
  const res = JSON.parse(response.body);
  const n = res.count;
  let nFilms = 0;
  let characters;
  const charUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
  for (let j = 0; j < n; j++) {
    characters = res.results[j].characters;
    for (let k = 0; k < characters.length; k++) {
      if (characters[k] === charUrl) {
        nFilms += 1;
      }
    }
  }
  console.log(nFilms);
});
