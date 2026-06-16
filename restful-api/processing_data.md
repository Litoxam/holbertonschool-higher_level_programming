# Consuming and Processing Data from an API with Python

## Overview

This project demonstrates how to:

* Send HTTP requests using the `requests` library.
* Retrieve data from a REST API.
* Parse JSON responses into Python objects.
* Manipulate data using lists and dictionaries.
* Export structured data to a CSV file.

The API used is:

```
https://jsonplaceholder.typicode.com/posts
```

---

# Imported Modules

## requests

```python
import requests
```

The `requests` library is used to communicate with web servers through HTTP.

Example:

```python
response = requests.get(url)
```

This sends an HTTP GET request and returns a `Response` object.

---

## csv

```python
import csv
```

The `csv` module allows Python to read and write CSV (Comma-Separated Values) files.

---

# Functions

## fetch_and_print_posts()

```python
def fetch_and_print_posts():
```

Retrieves posts from the API and prints their titles.

### requests.get()

```python
response = requests.get(url)
```

Sends an HTTP GET request.

Returns a `Response` object containing:

* Status code
* Headers
* Response body

---

### response.status_code

```python
response.status_code
```

Returns the HTTP status code.

Common codes:

| Code | Meaning      |
| ---- | ------------ |
| 200  | Success      |
| 404  | Not Found    |
| 500  | Server Error |

Example:

```python
print(f"Status Code: {response.status_code}")
```

---

### response.json()

```python
posts = response.json()
```

Converts the JSON response into Python objects.

The API returns JSON:

```json
[
  {
    "id": 1,
    "title": "...",
    "body": "..."
  }
]
```

After `.json()`, Python receives:

```python
[
    {
        "id": 1,
        "title": "...",
        "body": "..."
    }
]
```

This is a list of dictionaries.

---

### for loop

```python
for post in posts:
```

Iterates over each post.

Each `post` is a dictionary:

```python
{
    "id": 1,
    "title": "...",
    "body": "..."
}
```

---

### Dictionary access

```python
post["title"]
```

Retrieves the value associated with the key `"title"`.

---

## fetch_and_save_posts()

```python
def fetch_and_save_posts():
```

Retrieves posts and stores them in a CSV file.

---

### Empty list creation

```python
data = []
```

Creates an empty list.

---

### append()

```python
data.append(...)
```

Adds an element to the end of the list.

Example:

```python
numbers = []

numbers.append(1)
numbers.append(2)
```

Result:

```python
[1, 2]
```

---

### Dictionaries

```python
{
    "id": post["id"],
    "title": post["title"],
    "body": post["body"]
}
```

Creates a dictionary containing three key-value pairs.

Example:

```python
{
    "id": 1,
    "title": "Hello",
    "body": "World"
}
```

---

### with open()

```python
with open("posts.csv", "w", newline="", encoding="utf-8") as file:
```

Opens a file in write mode.

Parameters:

* `"posts.csv"` → file name.
* `"w"` → write mode.
* `newline=""` → avoids blank lines in CSV files.
* `encoding="utf-8"` → supports special characters.

Using `with` automatically closes the file when finished.

---

### csv.DictWriter()

```python
writer = csv.DictWriter(
    file,
    fieldnames=["id", "title", "body"]
)
```

Creates an object capable of writing dictionaries into a CSV file.

The column names are defined by:

```python
fieldnames=["id", "title", "body"]
```

---

### writeheader()

```python
writer.writeheader()
```

Writes the first line of the CSV file:

```csv
id,title,body
```

---

### writerows()

```python
writer.writerows(data)
```

Writes all dictionaries stored in the list.

Example:

```python
[
    {
        "id": 1,
        "title": "Title 1",
        "body": "Body 1"
    },
    {
        "id": 2,
        "title": "Title 2",
        "body": "Body 2"
    }
]
```

Produces:

```csv
id,title,body
1,Title 1,Body 1
2,Title 2,Body 2
```

---

# Data Flow

```
API
 ↓
requests.get()
 ↓
Response object
 ↓
response.json()
 ↓
List of dictionaries
 ↓
Data processing
 ↓
csv.DictWriter()
 ↓
posts.csv
```

---

# Concepts Used

* HTTP GET requests
* Response objects
* JSON parsing
* Lists
* Dictionaries
* For loops
* append()
* File handling
* Context managers (`with`)
* CSV generation
* `DictWriter`
