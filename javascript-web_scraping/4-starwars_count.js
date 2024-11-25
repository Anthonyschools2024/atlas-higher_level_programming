#!/usr/bin/node
const fetch = require('node-fetch');

const apiUrl = process.argv[2]; 
const wedgeAntillesId = '18';

fetch(apiUrl)
  .then(response => response.json())
  .then(data => {
    const films = data.results;
    const wedgeAntillesCount = films.reduce((count, film) => {
      return film.characters.includes(`https://swapi-api.hbtn.io/api/people/${wedgeAntillesId}/`)
        ? count + 1
        : count;
    }, 0);
    console.log(wedgeAntillesCount);
  })
  .catch(error => {
    console.error('Error:', error);
  });