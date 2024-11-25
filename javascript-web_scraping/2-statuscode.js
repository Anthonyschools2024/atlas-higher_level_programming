#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (error, response) => {
  if (error) {
    console.error('Error:', error); // Print error if one occurred
  } else {
    console.log('code:', response.statusCode); // Print the response status code
  }
});