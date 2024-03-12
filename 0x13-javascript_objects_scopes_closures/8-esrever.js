#!/usr/bin/node

exports.esrever = function (list) {
  const revList = [];
  if (list) {
    for (let j = 0; j < list.length; j++) {
      revList[j] = list[list.length - j - 1];
    }
  }

  return revList;
};
