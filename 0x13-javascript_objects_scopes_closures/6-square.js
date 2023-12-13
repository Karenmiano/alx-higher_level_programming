#!/usr/bin/node

const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c = 'X') {
    const sym = c.repeat(this.width);
    for (let i = 1; i <= this.height; i++) {
      console.log(sym);
    }
  }
}
module.exports = Square;
