#!/usr/bin/node
exports.callMeMoby = function (a, c) {
  for (let i = 0; i < a; i++) {
    c();
  }
};
