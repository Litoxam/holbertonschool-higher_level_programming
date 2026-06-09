# SQLAlchemy Cheat Sheet

## Session

```python
Session = sessionmaker(bind=engine)
session = Session()
```

- Create a session to interact with the database.

---

## Query

```python
session.query(State)
```

- Create a SQL query using SQLAlchemy ORM.

SQL equivalent:

```sql
SELECT * FROM states;
```

---

## Retrieve all rows

```python
session.query(State).all()
```

- Execute the query and return a list of objects.

SQL equivalent:

```sql
SELECT * FROM states;
```

---

## Sort rows

```python
session.query(State).order_by(State.id)
```

- Sort results in ascending order.

SQL equivalent:

```sql
SELECT * FROM states
ORDER BY id;
```

---

## Filter rows

```python
session.query(State).filter(State.id > 5).all()
```

- Add a WHERE condition.

SQL equivalent:

```sql
SELECT * FROM states
WHERE id > 5;
```

---

## Exact match

```python
session.query(State).filter(State.name == "Texas").all()
```

- Retrieve rows whose name is exactly "Texas".

SQL equivalent:

```sql
SELECT * FROM states
WHERE name = 'Texas';
```

---

## Filter rows with LIKE

```python
session.query(State).filter(State.name.like('%a%')).all()
```

- Retrieve rows whose name contains the letter `a`.

SQL equivalent:

```sql
SELECT * FROM states
WHERE name LIKE '%a%';
```

---

## Starts with

```python
session.query(State).filter(State.name.like('N%')).all()
```

- Retrieve rows whose name starts with `N`.

SQL equivalent:

```sql
SELECT * FROM states
WHERE name LIKE 'N%';
```

---

## Ends with

```python
session.query(State).filter(State.name.like('%a')).all()
```

- Retrieve rows whose name ends with `a`.

SQL equivalent:

```sql
SELECT * FROM states
WHERE name LIKE '%a';
```

---

## Contains

```python
session.query(State).filter(State.name.like('%n%')).all()
```

- Retrieve rows whose name contains `n`.

SQL equivalent:

```sql
SELECT * FROM states
WHERE name LIKE '%n%';
```