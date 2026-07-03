#!/usr/bin/node

const header = document.querySelector('header');
//when user clicks on 'red_header''s text, the .red class is added to header
const color_on_click = document.getElementById('red_header');
color_on_click.addEventListener('click', function() {
    header.classList.add('red');
});