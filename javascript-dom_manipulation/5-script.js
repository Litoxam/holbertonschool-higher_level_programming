#!/usr/bin/node

const header = document.querySelector('header');
const change_header = document.getElementById('update_header');

change_header.addEventListener('click', function(){
    header.textContent = 'New Header!!!';
})