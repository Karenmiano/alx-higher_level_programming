#!/usr/bin/node

const SquareO = require('./5-square');

class Square extends SquareO {
  charPrint (c = 'X') {
    for (let s = c, i = 1; i <= this.height; i++) {
      console.log(s.repeat(this.width));
    }
  }
}

module.exports = Square;
