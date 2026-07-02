#!/usr/bin/node

const headerNode = document.querySelector('header');
const red_on_click = document.getElementById('red_header');
function changeColor () {
    headerNode.style.color = '#FF0000';
}
red_on_click.addEventListener('click', changeColor);