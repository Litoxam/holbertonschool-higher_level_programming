#!/usr/bin/node

const args = process.argv;
const x = args[2];

if (isNaN(x)) {
  console.log('Missing size');
}

let line = '';
let i = 1;
let j = 1;
while (j <= x) {
  while (i <= x) {
    line += 'X';
    i++;
  }
  console.log(line);
  j++;
}
