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
session.query(State).filter(State.id > 5)
```

- Add a WHERE condition.

SQL equivalent:

```sql
SELECT * FROM states
WHERE id > 5;
```

---

## First row

```python
session.query(State).first()
```

- Return the first object.

SQL equivalent:

```sql
SELECT * FROM states
LIMIT 1;
```

---

## Count rows

```python
session.query(State).count()
```

- Count the number of rows.

SQL equivalent:

```sql
SELECT COUNT(*) FROM states;
```

---

## Add an object

```python
session.add(obj)
session.commit()
```

SQL equivalent:

```sql
INSERT INTO ...
```

---

## Delete an object

```python
session.delete(obj)
session.commit()
```

SQL equivalent:

```sql
DELETE FROM ...
```

---

## Save changes

```python
session.commit()
```

- Persist changes to the database.

---

## Cancel changes

```python
session.rollback()
```

- Undo uncommitted changes.

---

## Close session

```python
session.close()
```

- Release the database connection.