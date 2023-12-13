#!/usr/bin/node

exports.esrever = function (list) {
  let len = [];
  for (let ele of list) {
    len.unshift(ele);
  }
  return len;
};