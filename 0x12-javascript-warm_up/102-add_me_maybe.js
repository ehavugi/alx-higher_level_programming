#!/usr/bin/node
exports.addMeMaybe = function (a, c) {
  a = a + 1;
  c(a);
};
