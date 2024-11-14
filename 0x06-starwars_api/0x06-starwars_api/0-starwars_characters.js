#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

// star wars base url
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// get the movie details using star wars movie id
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching data:', error);
    return;
  }

  if (response.statusCode === 200) {
    const movieData = JSON.parse(body);

    const characters = movieData.characters;
//fetch character
    const fetchCharacter = (url) => {
      return new Promise((resolve, reject) => {
        request(url, (error, response, body) => {
          if (error) {
            reject('Error fetching character data:', error);
            return;
          }

          if (response.statusCode === 200) {
            const characterData = JSON.parse(body);
            console.log(characterData.name);
            resolve();
          } else {
            reject('Failed to fetch character data');
          }
        });
      });
    };

    (async () => {
      for (const characterUrl of characters) {
        await fetchCharacter(characterUrl);
      }
    })();
  } else {
    console.log(`Failed to fetch movie data. Status code: ${response.statusCode}`);
  }
});
