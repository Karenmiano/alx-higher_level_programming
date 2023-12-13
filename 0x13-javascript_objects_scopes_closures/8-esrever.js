#!/usr/bin/node

exports.esrever = function (list) {
  const len = [];
  for (const ele of list) {
    len.unshift(ele);
  }
  return len;
};
