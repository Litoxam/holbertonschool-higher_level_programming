#!/usr/bin/node

const args = process.argv;
const x = parseInt(args[2]);

function factorial (n) {
  if (n === 0 || n === 1 || isNaN(n)) {
    return 1;
  }
  return n * factorial(n - 1);
}

console.log(factorial(x));
