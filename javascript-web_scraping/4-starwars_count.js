#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
const wedgeAntillesId = '18';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const films = JSON.parse(body).results;
    const wedgeAntillesCount = films.reduce((count, film) => {
      return film.characters.includes(`https://swapi-api.hbtn.io/api/people/${wedgeAntillesId}/`)
        ? count + 1
        : count;
    }, 0);
    console.log(wedgeAntillesCount);
  }
});