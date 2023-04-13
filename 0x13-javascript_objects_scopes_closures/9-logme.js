#!/usr/bin/node
let index = 0;
exports.logMe = function (item) {
  console.log(String(index) + ': ' + String(item));
  index = index + 1;
};
