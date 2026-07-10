# Simple Templating Program

## Objective

The goal of this project is to create a Python function that generates personalized invitation files from a template and a list of attendees.

Each attendee receives their own invitation with the appropriate information inserted into the template.

---

# How It Works

The function receives two parameters:

* `template`: a string containing placeholders.
* `attendees`: a list of dictionaries containing attendee information.

Example template:

```text
Hello {name},

You are invited to the {event_title} on {event_date} at {event_location}.

We look forward to your presence.

Best regards,
Event Team
```

Example data:

```python
attendees = [
    {
        "name": "Alice",
        "event_title": "Python Conference",
        "event_date": "2023-07-15",
        "event_location": "New York"
    },
    {
        "name": "Bob",
        "event_title": "Data Science Workshop",
        "event_date": "2023-08-20",
        "event_location": "San Francisco"
    }
]
```

The program generates:

```text
output_1.txt
output_2.txt
...
```

Each file contains a personalized invitation.

---

# Concepts Learned

## 1. Input Validation with `isinstance()`

Before processing any data, the program validates the types of the arguments.

```python
if not isinstance(template, str):
    return
```

`isinstance()` checks whether an object belongs to a specific type.

Examples:

```python
isinstance("Hello", str)      # True
isinstance([], list)          # True
isinstance({}, dict)          # True
```

---

## 2. Data Validation

The function checks several conditions before continuing:

* The template must be a string.
* The template must not be empty.
* `attendees` must be a list.
* Every element of `attendees` must be a dictionary.
* The attendee list must not be empty.

These validations prevent the program from crashing because of invalid input.

---

## 3. Working with Dictionaries

Each attendee is represented as a dictionary.

Example:

```python
{
    "name": "Alice",
    "event_title": "Python Conference",
    "event_date": "2023-07-15",
    "event_location": "New York"
}
```

The `get()` method is used to retrieve values safely.

```python
attendee.get("name")
```

Unlike dictionary indexing:

```python
attendee["name"]
```

`get()` returns `None` instead of raising an exception if the key does not exist.

---

## 4. Default Values Using `or`

Missing values or `None` are replaced with `"N/A"`.

```python
name = attendee.get("name") or "N/A"
```

Examples:

```python
None or "N/A"
```

returns:

```text
N/A
```

```python
"Alice" or "N/A"
```

returns:

```text
Alice
```

This is a common Python pattern for assigning default values.

---

## 5. Iterating with `enumerate()`

Instead of manually counting iterations, the program uses `enumerate()`.

```python
for i, attendee in enumerate(attendees, start=1):
```

This provides:

* the index (`i`)
* the current attendee (`attendee`)

Example:

```text
1 → Alice
2 → Bob
3 → Charlie
```

The index is used to generate output file names.

---

## 6. f-Strings

f-strings provide a clean way to insert variables into strings.

```python
filename = f"output_{i}.txt"
```

Result:

```text
output_1.txt
```

They are the recommended string formatting method in modern Python.

---

## 7. The `replace()` Method

The template is personalized using the `replace()` string method.

Before:

```text
Hello {name}
```

After:

```text
Hello Alice
```

Example:

```python
invitation = invitation.replace("{name}", name)
```

Each placeholder is replaced individually.

---

## 8. String Immutability

Strings cannot be modified directly.

This code does **not** change the original string:

```python
invitation.replace("{name}", name)
```

Instead, the returned value must be assigned back:

```python
invitation = invitation.replace("{name}", name)
```

Understanding string immutability is an important Python concept.

---

## 9. File Handling

The program creates one output file per attendee.

```python
with open(filename, "w") as file:
    file.write(invitation)
```

The `"w"` mode:

* creates the file if it does not exist;
* overwrites the file if it already exists.

Using `with` automatically closes the file after writing.

---

## 10. The `os` Module

The `os` module allows interaction with the operating system.

Example:

```python
import os

if os.path.exists(filename):
    os.remove(filename)
```

Functions used:

* `os.path.exists()` checks whether a file exists.
* `os.remove()` deletes a file.

---

# Algorithm Overview

1. Validate the input types.
2. Check that the template is not empty.
3. Check that the attendee list is not empty.
4. Iterate through each attendee.
5. Copy the template.
6. Replace the placeholders.
7. Replace missing values with `"N/A"`.
8. Generate an output file name.
9. Write the personalized invitation to a text file.

---

# Skills Acquired

This project reinforces several core Python concepts:

* Input validation
* Dictionary manipulation
* List iteration
* Using `enumerate()`
* String manipulation
* Default values
* File creation and writing
* Basic interaction with the operating system
* Building a complete program by combining multiple Python concepts
