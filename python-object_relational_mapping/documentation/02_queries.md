# Queries

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