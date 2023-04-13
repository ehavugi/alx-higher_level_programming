#!/usr/bin/node
const Square0 = require('./5-square');

class Square extends Square0 {
  charPrint (c) {
    if (c !== undefined) {
      for (let i = 1; i <= this.height; i++) {
        console.log(String(c).repeat(this.width));
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
