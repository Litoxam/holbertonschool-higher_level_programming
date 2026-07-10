# Dynamic JSON Rendering

## Objective

The goal of this project is to learn how to read data from a **JSON** file and display it dynamically in a web page using **Flask** and **Jinja2**.

Instead of hardcoding HTML content, the application loads data from an external file and passes it to a template for rendering.

---

# Project Structure

```text
project/
│
├── task_02_logic.py
├── items.json
│
└── templates/
    ├── header.html
    ├── footer.html
    └── items.html
```

---

# New Concepts Learned

## 1. Reading JSON Files

Python's built-in `json` module makes it easy to read structured data.

Example:

```python
with open("items.json", "r") as file:
    data = json.load(file)
```

`json.load()` converts the JSON file into Python objects.

For example:

```json
{
    "items": [
        "Python Book",
        "Flask Mug",
        "Jinja Sticker"
    ]
}
```

becomes:

```python
{
    "items": [
        "Python Book",
        "Flask Mug",
        "Jinja Sticker"
    ]
}
```

---

## 2. Using `get()` with Dictionaries

The data loaded from the JSON file is stored as a dictionary.

Example:

```python
items = data.get("items", [])
```

Using `get()` prevents errors if the key does not exist.

If `"items"` is missing, an empty list (`[]`) is returned instead.

---

## 3. Passing Data to Templates

Flask can send Python variables directly to a Jinja template.

Example:

```python
return render_template(
    "items.html",
    items=items
)
```

The variable `items` becomes available inside the HTML template.

---

## 4. Jinja `for` Loops

Jinja allows iteration over Python lists.

Example:

```html
{% for item in items %}
<li>{{ item }}</li>
{% endfor %}
```

This generates one `<li>` element for every item in the list.

---

## 5. Conditional Rendering

Templates can display different content depending on the data.

Example:

```html
{% if items %}
```

If the list contains elements, they are displayed.

Otherwise:

```html
<p>No items found</p>
```

is rendered.

This avoids displaying an empty list.

---

## 6. Dynamic Content

Instead of writing HTML manually for every product or item, the page adapts automatically to the data received.

Adding a new value to `items.json` immediately updates the page without changing the template.

This separates the **data** from the **presentation**.

---

# Data Flow

```text
items.json
      │
      ▼
json.load()
      │
      ▼
Python list
      │
      ▼
render_template()
      │
      ▼
items.html
      │
      ▼
Dynamic HTML page
```

---

# Skills Acquired

This project reinforces several important Flask and Jinja concepts:

* Reading JSON files with Python.
* Converting JSON into Python objects.
* Passing variables from Flask to templates.
* Using Jinja `for` loops.
* Using Jinja `if` statements.
* Rendering dynamic HTML based on external data.
* Separating application logic from presentation.
