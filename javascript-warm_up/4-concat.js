#!/usr/bin/node

const args = process.argv;

if (args[2]) {
  console.log('c is ' + args[2]);
} else {
  console.log('c is undefined');
}
