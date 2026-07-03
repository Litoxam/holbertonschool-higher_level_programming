#!/usr/bin/node

const header = document.querySelector('header');
// when user clicks on 'red_header''s text, the .red class is added to header
const ColorOnClick = document.getElementById('red_header');
ColorOnClick.addEventListener('click', function () {
  header.classList.add('red');
});
