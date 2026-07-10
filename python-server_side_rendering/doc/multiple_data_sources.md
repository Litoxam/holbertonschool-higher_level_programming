# Multiple Data Sources

## Objective

The goal of this project is to build a Flask application capable of displaying the same data from multiple sources.

Instead of relying on a single file format, the application can load products from either a **JSON** file or a **CSV** file while using the same HTML template.

Users can also filter products by their ID using URL query parameters.

---

# Project Structure

```text
project/
│
├── task_03_files.py
├── products.json
├── products.csv
│
└── templates/
    └── product_display.html
```

---

# New Concepts Learned

## 1. URL Query Parameters

Flask allows access to parameters passed in the URL.

Example:

```python
source = request.args.get("source")
product_id = request.args.get("id")
```

For the following URL:

```text
/products?source=json&id=2
```

The variables contain:

```python
source = "json"
product_id = "2"
```

Query parameters make it possible to change the application's behavior without creating additional routes.

---

## 2. Reading CSV Files

Python provides the built-in `csv` module for working with CSV files.

Example:

```python
with open("products.csv", "r") as file:
    products = list(csv.DictReader(file))
```

`DictReader` converts each row into a dictionary.

Example:

```csv
id,name,category,price
1,Laptop,Electronics,799.99
```

becomes:

```python
{
    "id": "1",
    "name": "Laptop",
    "category": "Electronics",
    "price": "799.99"
}
```

---

## 3. Using Multiple Data Sources

The application decides which file to read based on the `source` parameter.

Example:

```python
if source == "json":
    ...
elif source == "csv":
    ...
```

Regardless of the selected source, the application always produces the same `products` list.

This allows the template to remain unchanged.

---

## 4. Filtering Data

Users can request a specific product by providing its ID.

Example:

```text
/products?source=json&id=2
```

The application iterates through the products and keeps only the matching item.

If no ID is provided, every product is displayed.

---

## 5. Error Handling

The application validates the user's request before displaying the page.

Possible cases include:

* Invalid data source.
* Product ID not found.

Instead of crashing, the application displays an appropriate message inside the template.

Examples:

```text
Wrong source
```

```text
Product not found
```

---

## 6. Reusing the Same Template

No matter where the data comes from, the application always renders:

```python
render_template(
    "product_display.html",
    products=products
)
```

The template does not need to know whether the data originated from JSON or CSV.

This is an example of separating the application's logic from its presentation.

---

# Data Flow

```text
                JSON
                  │
                  ▼
             json.load()

CSV ─────► DictReader()
                  │
                  ▼
            products list
                  │
                  ▼
        render_template()
                  │
                  ▼
      product_display.html
                  │
                  ▼
          Dynamic HTML table
```

---

# Skills Acquired

This project reinforces several important Flask concepts:

* Reading CSV files with Python.
* Using URL query parameters.
* Filtering data dynamically.
* Handling user input safely.
* Displaying error messages.
* Reusing a single template for multiple data sources.
* Keeping application logic separate from presentation.
