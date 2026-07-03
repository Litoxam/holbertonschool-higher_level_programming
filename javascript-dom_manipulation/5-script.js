#!/usr/bin/node

const header = document.querySelector('header');
const ChangeHeader = document.getElementById('update_header');

ChangeHeader.addEventListener('click', function () {
  header.textContent = 'New Header!!!';
});
