#!/usr/bin/node

const list = document.querySelector('.my_list');
const AddItem = document.getElementById('add_item');

AddItem.addEventListener('click', function () {
  const NewItem = document.createElement('li'); // name of tag
  NewItem.textContent = 'Item'; // content of tag
  list.appendChild(NewItem); // add new item at the end of .my_list
});
