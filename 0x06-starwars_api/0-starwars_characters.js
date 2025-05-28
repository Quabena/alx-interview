#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  function fetchCharacter(index) {
    if (index >= characters.length) return;

    request(characters[index], (err2, res2, body2) => {
      if (err2) {
        console.error(err2);
        return;
      }

      const character = JSON.parse(body2);
      console.log(character.name);
      fetchCharacter(index + 1);
    });
  }

  fetchCharacter(0);
});
