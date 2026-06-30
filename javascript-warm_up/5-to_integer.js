#!/usr/bin/node

const args = process.argv;
const numb = parseInt(args[2]);
if (numb) {
  console.log('My number: ' + numb);
} else {
  console.log('Not a number');
}
