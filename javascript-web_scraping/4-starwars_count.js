#!/usr/bin/node
const fetch = require('node-fetch');

const apiUrl = process.argv[2] || 'https://swapi-api.hbtn.io/api/films/'; // Default URL added
const wedgeAntillesId = 18; // Corrected to numeric ID

fetch(apiUrl)
  .then(response => response.json())
  .then(data => {
    const films = data.results;
    const wedgeAntillesCount = films.reduce((count, film) => {
      // Use numeric ID in the URL
      return film.characters.includes(`https://swapi-api.hbtn.io/api/people/${wedgeAntillesId}/`)
        ? count + 1
        : count;
    }, 0);
    console.log(wedgeAntillesCount);
  })
  .catch(error => {
    console.error('Error:', error);
  });