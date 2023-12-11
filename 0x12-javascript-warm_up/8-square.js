#!/usr/bin/node

const times = parseInt(process.argv[2], 10);
if (!isNaN(times)) {
  for (let c = 'X', i = 1; i <= times; i++) {
    console.log(c.repeat(times));
  }
} else {
  console.log('Missing size');
}
