# JOIN (Joining Tables)

## Query with JOIN

```python
cities = (
    session.query(City, State)
    .join(State, City.state_id == State.id)
    .order_by(City.id)
    .all()
)
```

---

## Select Multiple Models

```python
session.query(City, State)
```

Returns a tuple `(City, State)` for each result.

---

## Perform the Join

```python
.join(State, City.state_id == State.id)
```

SQL equivalent:

```sql
JOIN states
ON cities.state_id = states.id
```

---

## Sort the Results

```python
.order_by(City.id)
```

Sorts the cities by their ID.

---

## Retrieve All Results

```python
.all()
```

Returns a list of tuples:

```python
[
    (<City>, <State>),
    (<City>, <State>),
    ...
]
```

---

## Iterating Through the Results

```python
for city, state in cities:
    print("{}: ({}) {}".format(state.name, city.id, city.name))
```

Accessing attributes:

```python
city.id
city.name
state.id
state.name
```

---

## SQL Equivalent

```sql
SELECT cities.id,
       cities.name,
       states.id,
       states.name
FROM cities
JOIN states
    ON cities.state_id = states.id
ORDER BY cities.id;
```

---

## Simplified JOIN (Using relationship())

If a `relationship()` has been defined between the models:

```python
cities = (
    session.query(City)
    .join(State)
    .order_by(City.id)
    .all()
)

for city in cities:
    print(city.state.name, city.name)
```

This syntax requires a `relationship()` between `City` and `State`.

---

## INNER JOIN Diagram

```text
City table                    State table

+----+---------------+        +----+------------+
| id | state_id      |        | id | name       |
+----+---------------+        +----+------------+
| 1  | 1             | -----> | 1  | California |
| 2  | 1             | -----> | 1  | California |
| 3  | 2             | -----> | 2  | Arizona    |
+----+---------------+        +----+------------+

            JOIN

Result:

(City(id=1), State(id=1))
(City(id=2), State(id=1))
(City(id=3), State(id=2))
```
