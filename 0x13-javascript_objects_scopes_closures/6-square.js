#!/usr/bin/node

const Square = require('./5-square');

class Square1 extends Square {
  charPrint (c) {
    if (c === undefined) {
      return super.print(this.text);
    } else {
      const text = c;
      for (let i = 0; i < this.height; i++) {
        console.log(text.repeat(this.width));
      }
    }
  }
}

module.exports = Square1;
