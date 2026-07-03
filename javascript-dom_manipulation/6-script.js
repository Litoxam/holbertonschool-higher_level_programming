#!/usr/bin/node

const character = document.getElementById('character');

fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
  .then(function (response) {
    return response.json(); // GET all the data
  })
  .then(function (data) {
    character.textContent = data.name; // GET the value of .name
  });
