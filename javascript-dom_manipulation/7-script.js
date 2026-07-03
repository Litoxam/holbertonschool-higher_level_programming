#!/usr/bin/node

const listMovies = document.getElementById('list_movies');

fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(function (response) {
    return response.json(); // GET all the data
  })
  .then(function (data) {
    for (let i = 0; i < data.results.length; i++) {
      const newFilm = document.createElement('li');
      newFilm.textContent = data.results[i].title;
      listMovies.appendChild(newFilm);
    }
  });
