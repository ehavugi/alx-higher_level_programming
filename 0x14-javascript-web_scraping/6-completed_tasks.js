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
  const n = res.length;
  let user;
  const users = {};
  let completed;
  for (let j = 0; j < n; j++) {
    user = res[j].userId;
    completed = res[j].completed;
    if (completed) {
      if (users[user]) {
        users[user] += 1;
      } else {
        users[user] = 1;
      }
    }
  }
  console.log(users);
});
