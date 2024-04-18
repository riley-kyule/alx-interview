#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
const filmUrl = `https://swapi-api.alx-tools.com/api/films/${filmId}/`;

request(filmUrl, async (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  try {
    const parsedData = JSON.parse(body);
    const characters = parsedData.characters;

    for (const characterUrl of characters) {
      const characterResponse = await getRequest(characterUrl);
      const characterData = JSON.parse(characterResponse.body);
      console.log(characterData.name);
    }
  } catch (parseError) {
    console.error('Error parsing data:', parseError);
  }
});

function getRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(response);
      }
    });
  });
}