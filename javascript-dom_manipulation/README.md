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

# Concepts Learned

Throughout this project, I learned how to:

* Select HTML elements.
* Modify CSS properties.
* Listen for user events.
* Manipulate CSS classes.
* Create interactive web pages using the DOM.
