# SQLite Integration

## Objective

The goal of this project is to extend the existing Flask application by adding **SQLite** as a third data source.

Instead of reading products only from JSON or CSV files, the application can now retrieve data directly from a relational database while keeping the same user interface.

---

# Project Structure

```text
project/
│
├── task_04_db.py
├── products.db
├── products.json
├── products.csv
│
└── templates/
    └── product_display.html
```

---

# New Concepts Learned

## 1. SQLite Databases

SQLite is a lightweight relational database stored in a single file.

Unlike JSON or CSV files, data is organized into **tables** composed of rows and columns.

Example:

```text
Products
-----------------------------------------------
| id | name        | category     | price      |
-----------------------------------------------
| 1  | Laptop      | Electronics  | 799.99     |
| 2  | Coffee Mug  | Home Goods   | 15.99      |
-----------------------------------------------
```

SQLite is included with Python through the built-in `sqlite3` module.

---

## 2. Connecting to a Database

Before executing SQL queries, a connection must be established.

Example:

```python
connection = sqlite3.connect("products.db")
```

Once the connection is no longer needed, it should be closed.

```python
connection.close()
```

Closing the connection releases system resources.

---

## 3. Executing SQL Queries

A cursor is used to communicate with the database.

Example:

```python
cursor = connection.cursor()

cursor.execute("SELECT * FROM Products")

products = cursor.fetchall()
```

* `cursor()` creates an object that executes SQL commands.
* `execute()` sends a SQL query to the database.
* `fetchall()` returns every matching row.

---

## 4. Using `sqlite3.Row`

By default, SQLite returns tuples.

Example:

```python
(1, "Laptop", 799.99, "Electronics")
```

Setting:

```python
connection.row_factory = sqlite3.Row
```

allows each row to behave like a dictionary.

Example:

```python
product["name"]
```

instead of:

```python
product[1]
```

This makes SQLite data compatible with the existing template used for JSON and CSV.

---

## 5. Reusing the Same Application Logic

The application now supports three different data sources:

* JSON
* CSV
* SQLite

Regardless of the source, the application always stores the result in the same variable:

```python
products
```

This means the template does not need to change.

---

## 6. Keeping One Template

The same template renders every data source.

Example:

```python
return render_template(
    "product_display.html",
    products=products
)
```

Whether the products come from JSON, CSV, or SQLite, the HTML page remains identical.

This demonstrates one of the main goals of server-side rendering: separating **data retrieval** from **presentation**.

---

# Data Flow

```text
          JSON
            │
            ▼
       json.load()

CSV ──► DictReader()
            │
            ▼
SQLite ─► SELECT * FROM Products
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

This project reinforces several important backend development concepts:

* Working with SQLite databases.
* Connecting to a database using `sqlite3`.
* Executing SQL queries.
* Retrieving query results with `fetchall()`.
* Using `sqlite3.Row` for dictionary-like access.
* Supporting multiple data sources with the same application.
* Reusing a single template regardless of where the data comes from.
* Separating data access from presentation.
