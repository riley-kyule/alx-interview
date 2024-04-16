#!/usr/bin/node

const axios = require('axios');

if (process.argv.length !== 3){
	console.log('Usage: ./0-starwars_characters.js <n>');
	process.exit(1);
}

const id = process.argv[2];
if (isNaN(id)) {
  console.log('<n> must be an integer');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

async function fetchData () {
  try {
    const response = await axios.get(url);
    const responseData = response.data;
    const characters = responseData.characters;

    for (const character of characters) {
      try {
        const response = await axios.get(character);
        const body = response.data;
        const name = body.name;
        console.log(name);
      } catch (error) {
        console.error(error);
      }
    }
  } catch (parseError) {
    console.error(parseError);
  }
}

fetchData();