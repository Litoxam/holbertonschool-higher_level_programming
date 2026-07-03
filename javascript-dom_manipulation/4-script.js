#!/usr/bin/node

const list = document.querySelector('.my_list');
const add_item = document.getElementById('add_item');

add_item.addEventListener('click', function()){
    const new_Item = document.createElement('li'); // name of tag
    new_Item.textContent = 'Item'; // content of tag
    list.appendChild(new_Item); // add new item at the end of .my_list
}