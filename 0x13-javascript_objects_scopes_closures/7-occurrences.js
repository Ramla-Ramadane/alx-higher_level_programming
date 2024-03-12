#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let i = 0;

  if (list && searchElement) {
    i = (list.filter(element => element === searchElement))
      .length;
  }

  return i;
};
