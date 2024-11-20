#!/usr/bin/node
// Access command line arguments using process.argv
const arg1 = process.argv[2];
const arg2 = process.argv[3];

// Use template literals for string interpolation
console.log(`${arg1} is ${arg2}`);