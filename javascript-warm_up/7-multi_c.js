#!/usr/bin/node

const args = process.argv;
const x = args[2];

if (isNaN(x)) {
  console.log('Missing number of occurrences');
}
let i = 0;
while (i < x) {
  console.log('C is fun');
  i++;
}
