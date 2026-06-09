# Filters

## Filter rows

```python
session.query(State).filter(State.id > 5).all()
```

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

SQL equivalent:

```sql
SELECT * FROM states
WHERE name LIKE '%n%';
```