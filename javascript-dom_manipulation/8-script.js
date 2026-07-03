#!/usr/bin/node

document.addEventListener('DOMContentLoaded', function () {
  const hello = document.getElementById('hello');

  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(function (response) {
      return response.json(); // GET all the data
    })
    .then(function (data) {
      hello.textContent = data.hello;
    });
});
