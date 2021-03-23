#!/usr/bin/node

exports.esrever = function (list) {
  const temp = [];
  let counter = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    temp[counter] = list[i];
    counter += 1;
  }
  return temp;
};
