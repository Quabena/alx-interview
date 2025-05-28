#!/usr/bin/node


const request = require('request');

const filmId = process.argv[2];
const apiUrl = 'https://swapi-api.hbtn.io/api/films/' + filmId;

request(apiUrl, (err, res, body) => {
  if (err) throw err;

  const filmData = JSON.parse(body);
  const charUrls = filmData.characters;

  printCharactersInOrder(charUrls, 0);
});

function printCharactersInOrder(list, index) {
  if (index >= list.length) return;

  request(list[index], (err, res, body) => {
    if (err) throw err;

    const charData = JSON.parse(body);
    console.log(charData.name);
    printCharactersInOrder(list, index + 1);
  });
}
