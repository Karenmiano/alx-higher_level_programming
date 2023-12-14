#!/usr/bin/node

const arr = require('./100-data').list;
const newarr = arr.map((x, idx) => x * idx);
console.log(arr);
console.log(newarr);
