#!/usr/bin/env node
const axios = require('axios');

// Validate the command-line arguments
if (process.argv.length !== 3) {
  console.log('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];

// Validate that the Movie ID is a number
if (isNaN(movieId)) {
  console.log('Movie ID must be a number');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

// Function to fetch and display character names
async function fetchCharacters() {
  try {
    const response = await axios.get(apiUrl);
    const movieData = response.data;

    if (!movieData.characters) {
      console.log('Invalid Movie ID');
      process.exit(1);
    }

    for (const characterUrl of movieData.characters) {
      const characterResponse = await axios.get(characterUrl);
      const characterData = characterResponse.data;
      console.log(characterData.name);
    }
  } catch (error) {
    console.error('Error:', error.message);
    process.exit(1);
  }
}

// Call the function
fetchCharacters();
