#!/usr/bin/node

module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    if (c) {
      for (let j = 0; j < this.height; j++) {
        console.log(c.repeat(this.width));
      }
    } else {
      this.print();
    }
  }
};
