#!/usr/bin/node
const myArg = process.argv[2];

if (parseInt(myArg)) {
  console.log('My number: ' + parseInt(myArg));
} else {
  console.log('Not a number');
}