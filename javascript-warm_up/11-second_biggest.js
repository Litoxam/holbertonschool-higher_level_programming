#!/usr/bin/node

const args = process.argv;
const numbers = [];

if (args.length < 4) {
  console.log('0');
} else {
  for (let i = 2; i < args.length; i++) { // push every argv into numbers[]
    numbers.push(parseInt(args[i]));
  }
  numbers.sort((a, b) => a - b);
  const nblength = numbers.length;
  console.log(numbers[nblength - 2]);
}
