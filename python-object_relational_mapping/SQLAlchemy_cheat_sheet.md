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

## INSERT / ADD OBJECTS

### Create a new object

```python
new_state = State(name="Louisiana")
```

### Add the object to the session

```python
session.add(new_state)
```

### Save changes to the database

```python
session.commit()
```

### Access the id assigned by MySQL

```python
print(new_state.id)
```

---

### Add multiple objects

```python
state1 = State(name="California")
state2 = State(name="Arizona")

session.add_all([state1, state2])
session.commit()
```

---

## UPDATE OBJECTS

### Retrieve an object

```python
state = session.query(State).filter(State.id == 1).first()
```

### Modify one or more attributes

```python
state.name = "New Mexico"
```

### Save changes

```python
session.commit()
```

---

## DELETE OBJECTS

### Retrieve an object

```python
state = session.query(State).filter(State.name == "Texas").first()
```

### Delete the object

```python
session.delete(state)
```

### Save changes

```python
session.commit()
```

---

## COMMON CRUD OPERATIONS

### Create

```python
new_state = State(name="Louisiana")
session.add(new_state)
session.commit()
```

### Read

```python
session.query(State).all()
session.query(State).first()
session.query(State).filter(State.name == "Texas").first()
session.query(State).order_by(State.id).all()
```

### Update

```python
state = session.query(State).filter(State.id == 1).first()
state.name = "New Mexico"
session.commit()
```

### Delete

```python
state = session.query(State).filter(State.id == 1).first()
session.delete(state)
session.commit()
```

### Close the session

```python
session.close()
```
