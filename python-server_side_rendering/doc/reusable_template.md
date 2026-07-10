# Reusable Templates with Flask

## Objective

The goal of this project is to learn how to reuse HTML components across multiple pages using **Flask** and **Jinja2** templates.

Instead of copying the same HTML into every page, common elements such as the **header** and **footer** are stored in separate template files and included where needed.

---

## Project Structure

```text
project/
│
├── app.py
└── templates/
    ├── header.html
    ├── footer.html
    ├── index.html
    ├── about.html
    └── contact.html
```

---

## New Concepts Learned

### Shared Templates

Common page elements can be placed in dedicated template files.

Example:

```html
{% include "header.html" %}
```

This inserts the content of `header.html` into the current page.

The same applies to:

```html
{% include "footer.html" %}
```

This approach follows the **DRY (Don't Repeat Yourself)** principle by avoiding duplicated code.

---

### Multiple Routes

Each page is associated with its own Flask route.

Example:

```python
@app.route('/about')
def about():
    return render_template('about.html')
```

When a user visits `/about`, Flask renders the corresponding template.

---

### render_template()

The `render_template()` function loads HTML files from the `templates/` directory.

Example:

```python
return render_template('contact.html')
```

There is no need to specify the `templates/` folder because Flask searches it automatically.

---

## Pages Created

* **Home** (`/`)
* **About** (`/about`)
* **Contact** (`/contact`)

Each page shares the same header and footer while displaying its own unique content.

---

## Key Takeaways

* Organize HTML into reusable components.
* Reduce duplicated code with Jinja's `include`.
* Create multiple pages using Flask routes.
* Keep templates clean and easier to maintain.
