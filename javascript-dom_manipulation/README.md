# JavaScript DOM Manipulation

This repository contains my solutions for the **JavaScript DOM Manipulation** project from Holberton School.

Each script demonstrates a different way to interact with the DOM using JavaScript.

---

# Table of Contents

* [0-script.js](#0-scriptjs)
* [1-script.js](#1-scriptjs)
* [2-script.js](#2-scriptjs)
* [3-script.js](#3-scriptjs)

---

# 0-script.js

**File:** [`0-script.js`](./0-script.js)

### Goal

Change the text color of the `<header>` element to red.

### Methods used

#### `document.querySelector()`

Selects the first element matching a CSS selector.

```javascript
const header = document.querySelector('header');
```

#### `element.style`

Modifies the inline CSS of an element.

```javascript
header.style.color = '#FF0000';
```

---

# 1-script.js

**File:** [`1-script.js`](./1-script.js)

### Goal

Change the header color when the user clicks on the element with the id `red_header`.

### New methods

#### `document.getElementById()`

Selects an element by its `id`.

```javascript
const button = document.getElementById('red_header');
```

#### `addEventListener()`

Executes a function when an event occurs.

```javascript
button.addEventListener('click', changeColor);
```

---

# 2-script.js

**File:** [`2-script.js`](./2-script.js)

### Goal

Add the CSS class `red` to the header when the user clicks on `red_header`.

### New methods

#### `classList.add()`

Adds a CSS class to an element.

```javascript
header.classList.add('red');
```

---

# 3-script.js

**File:** [`3-script.js`](./3-script.js)

### Goal

Toggle the header class between `red` and `green`.

### New methods

#### `classList.contains()`

Checks if an element contains a class.

```javascript
header.classList.contains('red');
```

Returns `true` or `false`.

#### `classList.replace()`

Replaces one class with another.

```javascript
header.classList.replace('red', 'green');
```

This ensures that the header always has exactly one class.

---

---

# 4-script.js

**File:** [`4-script.js`](./4-script.js)

### Goal

Add a new `<li>` element to the list every time the user clicks on the **Add item** button.

### New methods

#### `document.createElement()`

Creates a new HTML element.

```javascript
const newItem = document.createElement('li');
```

The element is created in memory and is not yet displayed on the page.

---

#### `textContent`

Gets or sets the text content of an HTML element.

```javascript
newItem.textContent = 'Item';
```

This sets the text displayed inside the `<li>` element.

---

#### `appendChild()`

Adds a new child element at the end of another element.

```javascript
list.appendChild(newItem);
```

In this exercise, each click appends a new `<li>` to the existing list.

---

# 5-script.js

**File:** [`5-script.js`](./5-script.js)

### Goal

Update the text of the `<header>` element when the user clicks on the button.

### New methods

#### `textContent`

Updates the text displayed inside an HTML element.

```javascript
header.textContent = 'New Header!!!';
```

Unlike `innerHTML`, `textContent` only modifies plain text and does not interpret HTML tags.

---

# 6-script.js

**File:** [`6-script.js`](./6-script.js)

### Goal

Retrieve data from the Star Wars API and display the character's name inside the page.

### New methods

#### `fetch()`

Sends an HTTP request and returns a **Promise**.

```javascript
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json');
```

It is commonly used to retrieve data from an external API.

---

#### `Promise`

A Promise represents the result of an asynchronous operation.

JavaScript continues executing the rest of the code while waiting for the server to respond.

---

#### `.then()`

Executes a function once the Promise has been resolved.

```javascript
fetch(url)
  .then(function (response) {
    return response.json();
  })
  .then(function (data) {
    console.log(data.name);
  });
```

Each `.then()` receives the value returned by the previous one.

---

#### `response.json()`

Converts the JSON response into a JavaScript object.

```javascript
response.json();
```

The returned object can then be accessed using its properties.

Example:

```javascript
data.name
```

returns:

```text
Leia Organa
```

This value is then displayed in the HTML page using `textContent`.


# Concepts Learned

Throughout this project, I learned how to:

* Select HTML elements.
* Modify CSS properties.
* Listen for user events.
* Manipulate CSS classes.
* Create interactive web pages using the DOM.
