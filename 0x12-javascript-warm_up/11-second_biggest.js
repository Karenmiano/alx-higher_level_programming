#!/usr/bin/node

function secondlargest (arr) {
  let first = -Infinity;
  let second = -Infinity;

  for (const num of arr) {
    if (num > first) {
      second = first;
      first = num;
    } else if (num > second && num !== first) {
      second = num;
    }
  }
  return (second);
}

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const newarr = process.argv.slice(2).map(Number);
  console.log(secondlargest(newarr));
}
