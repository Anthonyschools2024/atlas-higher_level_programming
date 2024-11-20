#!/usr/bin/node

// Get the list of arguments and convert them to integers
const args = process.argv.slice(2).map(Number);

// If no arguments or only one argument, print 0
if (args.length < 2) {
  console.log(0);
  process.exit(0);
}

// Sort the array in descending order
args.sort((a, b) => b - a);

// The second biggest element is at index 1
console.log(args[1]);