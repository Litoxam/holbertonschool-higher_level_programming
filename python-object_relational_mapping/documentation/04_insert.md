# INSERT / ADD OBJECTS

## Create a new object

```python
new_state = State(name="Louisiana")
```

## Add the object to the session

```python
session.add(new_state)
```

## Save changes

```python
session.commit()
```

## Access the id assigned by MySQL

```python
print(new_state.id)
```

---

## Add multiple objects

```python
state1 = State(name="California")
state2 = State(name="Arizona")

session.add_all([state1, state2])
session.commit()
```