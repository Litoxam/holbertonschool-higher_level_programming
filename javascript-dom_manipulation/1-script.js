#!/usr/bin/node

const headerNode = document.querySelector('header');
const redOnClick = document.getElementById('red_header');
function changeColor () {
  headerNode.style.color = '#FF0000';
}
redOnClick.addEventListener('click', changeColor);
