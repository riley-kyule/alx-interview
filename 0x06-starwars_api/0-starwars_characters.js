#!/usr/bin/node
/**
 * Prints all characters of a Star Wars movie
 * The first positional argument passed is the Movie ID
 * Display one character name per line in the same order
 * as  list in the /films/ endpoint
 */

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Error:', response.statusCode, response.statusMessage);
    process.exit(1);
  }

  const filmData = JSON.parse(body);

  // Display characters in the same order as the "characters" list in the /films/ endpoint
  filmData.characters.forEach((characterUrl) => {
    request(characterUrl, (characterError, characterResponse, characterBody) => {
      if (characterError) {
        console.error('Error:', characterError);
        process.exit(1);
      }

      if (characterResponse.statusCode !== 200) {
        console.error('Error:', characterResponse.statusCode, characterResponse.statusMessage);
        process.exit(1);
      }

      const characterData = JSON.parse(characterBody);
      console.log(characterData.name);
    });
  });
});
