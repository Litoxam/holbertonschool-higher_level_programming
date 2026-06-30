#!/usr/bin/node

const args = process.argv;
const x = parseInt(args[2]);
const y = parseInt(args[3]);
const sum = x + y;

function add (x, y) {
  console.log(sum);
}

add(x, y);
